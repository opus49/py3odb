"""Use ctypes to load libOdb.so and access symbols"""

import ctypes
from ctypes.util import find_library


_LIB = find_library("Odb")
if _LIB is None:
    raise OSError("Could not find libOdb.  Try updating your LD_LIBRARY_PATH.")
_ODBQL = ctypes.CDLL(_LIB)
_ODBQL.odbql_column_name.restype = ctypes.c_char_p
_ODBQL.odbql_column_text.restype = ctypes.c_char_p
_ODBQL.odbql_errmsg.restype = ctypes.c_char_p
_ODBQL.odbql_value_double.restype = ctypes.c_double


# globals
ODBQL_OK = 0
ODBQL_ERROR = 1
ODBQL_BUSY = 5
ODBQL_ROW = 100
ODBQL_DONE = 101
ODBQL_METADATA_CHANGED = 102
ODBQL_STATIC = ctypes.c_void_p(0)

# data types
ODBQL_INTEGER = 1
ODBQL_FLOAT = 2
ODBQL_TEXT = 3
ODBQL_BLOB = 4
ODBQL_NULL = 5
ODBQL_BITFIELD = 6


# functions
def odbql_bind_double(*args):
    """
    Bind double (Python float) values to prepared statements.
    ODBQL_API int odbql_bind_double(odbql_stmt*, int, double)
    """
    return _ODBQL.odbql_bind_double(*args)


def odbql_bind_int(*args):
    """
    Bind integer values to prepared statements.
    ODBQL_API int odbql_bind_int(odbql_stmt*, int, int)
    """
    return _ODBQL.odbql_bind_int(*args)


def odbql_bind_null(*args):
    """
    Bind NULL values to prepared statements.
    ODBQL_API int odbql_bind_null(odbql_stmt*, int)
    """
    return _ODBQL.odbql_bind_null(*args)


def odbql_bind_text(*args):
    """
    Bind string values to prepared statements.
    ODBQL_API int odbql_bind_text(odbql_stmt*, int, const char*, int, void(*), (void*))
    """
    return _ODBQL.odbql_bind_text(*args)


def odbql_close(*args):
    """
    Destroys odbql object.
    ODBQL_API int odbql_close(odbql*);
    """
    return _ODBQL.odbql_close(*args)


def odbql_column_count(*args):
    """
    Returns the number of columns in the result set returned by the prepared
    statement.  Returns zero if pStmt is an SQL statemement that does not
    return data (e.g. UPDATE).
    ODBQL_API int odbql_column_count(odbql_stmt *pStmt);
    """
    return _ODBQL.odbql_column_count(*args)


def odbql_column_name(*args):
    """
    Returns the name assigned to a particular column in the result set
    of a SELECT statement. N is the column number (starting at zero).
    ODBQL_API const char * odbql_column_name(odbql_stmt*, int N);
    """
    return _ODBQL.odbql_column_name(*args)


def odbql_column_text(*args):
    """
    Returns the referenced column as text.
    ODBQL_API unsigned char * odbql_column_text(odbql_stmt*, int iCol);
    """
    return _ODBQL.odbql_column_text(*args)


def odbql_column_type(*args):
    """
    Returns the datatype code for the initial data type of the result column.
    ODBQL_API int odbql_column_type(odbql_stmt*, int iCol);
    """
    return _ODBQL.odbql_column_type(*args)


def odbql_column_value(*args):
    """
    Returns the odbql_value object for the column.
    ODBQL_API odbql_value odbql_column_value(odbql_stmt*, int iCol);
    """
    return _ODBQL.odbql_column_value(*args)


def odbql_errmsg(*args):
    """
    If the most recent API call was unsuccessful, odbql_errmsg will return
    English-language text that describes the error.  Requires that
    odbql_errmsg.restype be set to ctypes.c_char_p.
    ODBQL_API const char * odbql_errmsg(odbql*);
    """
    return _ODBQL.odbql_errmsg(*args)


def odbql_finalize(*args):
    """
    Destroys a prepared statement object.
    ODBQL_API int odbql_finalize(odbql_stmt *pStmt);
    """
    return _ODBQL.odbql_finalize(*args)


def odbql_open(*args):
    """
    Creates odbql object.
    ODBQL_API int odbql_open(const char *filename, odbql **ppDb);
    """
    return _ODBQL.odbql_open(*args)


def odbql_prepare_v2(*args):
    """
    Compiles SQL query into byte-code program.
    ODBQL_API int odbql_prepare_v2(
        odbql *db,            /* Database handle */
        const char *zSql,     /* SQL statement, UTF-8 encoded */
        int nByte,            /* Maximum length of zSql in bytes. */
        odbql_stmt **ppStmt,  /* OUT: Statement handle */
        const char **pzTail   /* OUT: Pointer to unused portion of zSql */
    """
    return _ODBQL.odbql_prepare_v2(*args)


def odbql_step(*args):
    """
    Evaluates an SQL statement.  After a statement has been prepared, this
    function must be called one or more times to evaluate the statement.
    ODBQL_DONE means that the statement has finished executing successfully.
    obql_step() should not be called again without first calling odbql_reset().
    If the SQL statement returns any data, then ODBQL_ROW is returned each
    time a new row of data is ready for processing by the caller.  The values
    may be accessed by using the column access functions.
    ODBQL_API int odbql_step(odbql_stmt*);
    """
    return _ODBQL.odbql_step(*args)


def odbql_value_double(*args):
    """
    Converts an odbql_value object into a double.
    ODBQL_API double odbql_value_double(odbql_value*);
    """
    return _ODBQL.odbql_value_double(*args)


def odbql_value_int(*args):
    """
    Converts an odbql_value object into an integer.
    ODBQL_API int odbql_value_int(odbql_value*);
    """
    return _ODBQL.odbql_value_int(*args)
