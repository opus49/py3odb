"""Connection object and connect function"""

import ctypes
from warnings import warn

import py3odb.odbql as odbql
from .cursor import Cursor
from .error import InterfaceError, OperationalError


def connect(parameters):
    """
    Constructor for creating a connection to the database.
    Returns a Connection object.
    """
    return Connection(parameters)


class Connection:
    """A connection to the database"""
    def __init__(self, dsn):
        self._database = self._open(dsn)
        self._connected = True

    @staticmethod
    def _open(dsn):
        """Opens a connection to a database and returns an odbql object."""
        database = ctypes.c_void_p()
        retcode = odbql.odbql_open(dsn.encode("UTF-8"), ctypes.byref(database))
        if retcode == odbql.ODBQL_OK:
            return database
        raise InterfaceError(f"Cannot connect to dsn: {dsn}")

    @property
    def is_connected(self):
        """Read-only attribute for the the connection status."""
        return self._connected

    def close(self):
        """Close the connection now."""
        retcode = odbql.odbql_close(self._database)
        if retcode == odbql.ODBQL_OK:
            self._connected = False
        elif retcode == odbql.ODBQL_BUSY:
            warn("Connection to database is busy", RuntimeWarning)
        else:
            warn("Unable to close database", RuntimeWarning)

    def commit(self):
        """Commit any pending transaction to the database."""
        pass

    @property
    def database(self):
        """Reference to the underlying odbql database object."""
        return self._database

    def rollback(self):
        """Roll back to the start of any pending transaction."""
        pass

    def cursor(self):
        """Return a new Cursor object using the connection."""
        if self._connected:
            return Cursor(self)
        raise OperationalError("The database connection is closed.")
