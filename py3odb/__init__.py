"""
Python 3.6+ compatible interface to ECMWF's ODB API
"""

from .connection import connect, Connection
from .error import (
    Error, InterfaceError, DatabaseError, InternalError, OperationalError,
    ProgrammingError, IntegrityError, DataError, NotSupportedError
)

__all__ = [
    'connect',
    'Connection',
    'Error',
    'InterfaceError',
    'DatabaseError',
    'InternalError',
    'OperationalError',
    'ProgrammingError',
    'IntegrityError',
    'DataError',
    'NotSupportedError'
]

# https://www.python.org/dev/peps/pep-0249/#globals
# pylint: disable-msg=c0103
apilevel = '2.0'
threadsafety = 1
paramstyle = 'qmark'
# pylint: enable-msg=c0103
