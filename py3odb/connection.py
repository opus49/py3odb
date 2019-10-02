"""Connection object and connect function"""

import ctypes
from warnings import warn

import py3odb.odbql as odbql
from .cursor import Cursor
from .error import InterfaceError, OperationalError, NotSupportedError


def connect(filename):
    """
    Creates a connection to the database.
    """
    return Connection(filename)


class Connection:
    """
    A connection to the database.
    """
    def __init__(self, filename):
        self._database = self._open(filename)
        self._filename = filename
        self._connected = True
        self._cursors = []

    @staticmethod
    def _open(filename):
        """Opens a connection to a database and returns an odbql object."""
        database = ctypes.c_void_p()
        retcode = odbql.odbql_open(filename.encode("UTF-8"), ctypes.byref(database))
        if retcode == odbql.ODBQL_OK:
            return database
        raise InterfaceError(f"Cannot connect to filename: {filename}")

    @property
    def database(self):
        """Reference to the underlying odbql database object."""
        return self._database

    @property
    def is_connected(self):
        """Read-only attribute for the the connection status."""
        return self._connected

    @property
    def filename(self):
        """The filename representing the connected database."""
        return self._filename

    def close(self):
        """Close the connection now."""
        while self._cursors:
            self._cursors.pop().close()
        retcode = odbql.odbql_close(self._database)
        if retcode == odbql.ODBQL_OK:
            self._connected = False
        elif retcode == odbql.ODBQL_BUSY:
            warn("Connection to database is busy", RuntimeWarning)
        else:
            warn("Unable to close database", RuntimeWarning)

    @staticmethod
    def commit():
        """Commit any pending transaction to the database."""
        raise NotSupportedError("py3odb does not support transactions.")

    @staticmethod
    def rollback():
        """Roll back to the start of any pending transaction."""
        raise NotSupportedError("py3odb does not support rollback")

    def cursor(self):
        """Return a new Cursor object using the connection."""
        if self._connected:
            self._cursors.append(Cursor(self))
            return self._cursors[-1]
        raise OperationalError("The database connection is closed.")
