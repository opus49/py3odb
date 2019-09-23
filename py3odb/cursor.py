"""Cursor object"""

import ctypes
from warnings import warn

import py3odb.odbql as odbql
from .error import OperationalError, ProgrammingError, NotSupportedError


class Cursor:
    """
    A database cursor which is used to manage the context of a fetch operation.
    Cursors created from the same connection are not isolated.
    """
    def __init__(self, connection):
        self.arraysize = 1  # number of rows to fetch at a time with fetchmany
        self._closed = False
        self._column_count = 0
        self._connection = connection
        self._description = None
        self._stmt = None
        self._names = []
        self._types = []

    def _bind_parameters(self, parameters):
        """Bind parameters to an SQL statement"""
        if self._stmt is None:
            raise OperationalError("There is no prepared statement.")
        for index, parameter in enumerate(parameters):
            if parameter is None:
                retcode = odbql.odbql_bind_null(self._stmt, index)
            elif isinstance(parameter, str):
                encoded_parameter = parameter[:8].encode("UTF-8")
                retcode = odbql.odbql_bind_text(
                    self._stmt,
                    index,
                    encoded_parameter,
                    len(encoded_parameter),
                    odbql.ODBQL_STATIC
                )
            elif isinstance(parameter, int):
                retcode = odbql.odbql_bind_int(self._stmt, index, parameter)
            elif isinstance(parameter, float):
                retcode = odbql.odbql_bind_double(
                    self._stmt,
                    index,
                    ctypes.c_double(parameter)
                )
            else:
                raise ProgrammingError(f"Cannot bind parameter type {type(parameter)}")
            if retcode != odbql.ODBQL_OK:
                raise ProgrammingError(f"Parameter bind error")
        odbql.odbql_step(self._stmt)

    @staticmethod
    def _column_info(name, type_):
        return (name, type_, None, None, None, None, True)

    def _get_column(self, index):
        """Get the column value for the current row at the given index."""
        raw_value = odbql.odbql_column_value(self._stmt, index)
        if not raw_value:
            return None
        if self._types[index] == odbql.ODBQL_FLOAT:
            return odbql.odbql_value_double(raw_value)
        elif self._types[index] == odbql.ODBQL_INTEGER:
            return odbql.odbql_value_int(raw_value)
        elif self._types[index] == odbql.ODBQL_TEXT:
            return odbql.odbql_column_text(self._stmt, index).decode("UTF-8").strip()
        elif self._types[index] == odbql.ODBQL_BITFIELD:
            return odbql.odbql_value_int(raw_value)
        return None

    def _populate_metadata(self):
        """Generate the description for the most recent column results."""
        self._column_count = odbql.odbql_column_count(self._stmt)
        self._names = []
        self._types = []
        for index in range(self._column_count):
            self._names.append(odbql.odbql_column_name(self._stmt, index).decode("UTF-8"))
            self._types.append(odbql.odbql_column_type(self._stmt, index))
        if self._names and self._types:
            self._description = list(map(self._column_info, self._names, self._types))
        else:
            self._description = None

    def _prepare_statement(self, operation):
        """Prepare a database operation."""
        if not self._connection.is_connected:
            raise OperationalError("The database is not connected.")
        if self._closed:
            raise OperationalError("The cursor is closed.")
        if not operation.endswith(';'):
            operation += ';'
        if self._stmt is not None:
            self.finalize()
        self._stmt = ctypes.c_void_p(0)
        tail = ctypes.c_char_p(0)
        retcode = odbql.odbql_prepare_v2(
            self._connection.database,
            operation.encode("UTF-8"),
            -1,
            ctypes.byref(self._stmt),
            ctypes.byref(tail)
        )
        if retcode != odbql.ODBQL_OK:
            err = odbql.odbql_errmsg(self._connection.database).decode("UTF-8")
            raise ProgrammingError(err)

    @property
    def description(self):
        """
        Read-only attribute that is a sequence of 7-item sequences.  This class
        uses a list of tuples to describe column results.  The tuple elements
        will correspond to the following items:
            name
            type_code
            display_size
            internal_size
            precision
            scale
            null_ok

        Only the first two items (name and type_code) are mandatory, the other
        five are optional and set to None if no useful values can be provided.

        This attribute will be None for operations that do not return rows or
        if the cursor has not had an operation invoked in the execute method.

        The type_code can be interpreted by comparing it to the Type object.
        """
        return self._description

    @property
    def rowcount(self):
        """
        Read-only attribute specifies the number of rows that the last execute
        produced.  The attribute is -1 in case no execute has been performed on
        the cursor or the rowcount of the last operation cannot be determined.
        """
        raise NotSupportedError("rowcount is not supported by ODBQL")

    def close(self):
        """
        Close the cursor now.  The cursor will be unusable from this point
        forward and an exception will be raised if any operation is attempted.
        """
        self.finalize()
        self._closed = True  # TODO - do more garbage collection?

    def execute(self, operation, parameters=None):
        """
        Prepare and execute a database operation (query or command).
        ODBQL only supports parameterized INSERT statements and does not
        support parameterization of SELECT statements.  Parameters must be
        a sequence and will be bound to variables in the operation.
        """
        self._prepare_statement(operation)
        if parameters is not None:
            self._bind_parameters(parameters)
        else:
            self._populate_metadata()

    def executemany(self, operation, seq_of_parameters):
        """
        Prepare a database operation (query or command) and then execute
        it against all parameter sequences found in seq_of_parameters.
        """
        self._prepare_statement(operation)
        for parameters in seq_of_parameters:
            self._bind_parameters(parameters)

    def fetchone(self):
        """
        Fetch the next row of a query result set, returning a single sequence,
        or None when no more data is available.  A ProgrammingError is raised
        if the previous call to execute did not produce any result set or no
        call was issued yet.
        """
        if self._stmt is None:
            raise ProgrammingError("You must execute a statement first.")
        retcode = odbql.odbql_step(self._stmt)
        if retcode == odbql.ODBQL_METADATA_CHANGED or self.description is None:
            self._populate_metadata()
        if retcode not in (odbql.ODBQL_ROW, odbql.ODBQL_METADATA_CHANGED):
            return None
        return [self._get_column(index) for index in range(self._column_count)]

    def fetchmany(self, size=None):
        """
        Fetch the next set of rows of a query result, returning a sequence
        of sequences (e.g. a list of tuples).  An empty sequence is returned
        when no more rows are available.
        """
        if size is None:
            size = self.arraysize
        rows = []
        for _ in range(size):
            row = self.fetchone()
            if row:  # both not empty and not None
                rows.append(row)
            else:
                break
        return rows if rows else None

    def fetchall(self):
        pass

    def finalize(self):
        """Destroy the preapred statement object."""
        if self._stmt is not None:
            retcode = odbql.odbql_finalize(self._stmt)
            if retcode != odbql.ODBQL_OK:
                warn("Unable to finalize statement", RuntimeWarning)
            self._stmt = None

    def nextset(self):
        pass

    def setinputsizes(self, sizes):
        pass

    def setoutputsize(self, ):
        pass
