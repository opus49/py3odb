:mod:`py3odb.error`
===================

.. py:module:: py3odb.error

.. autoapi-nested-parse::

   Custom Exception classes for ODB
   https://www.python.org/dev/peps/pep-0249/#exceptions



Module Contents
---------------

.. py:exception:: Error

   Bases: :class:`Exception`

   Base class for ODB errors


.. py:exception:: InterfaceError

   Bases: :class:`py3odb.error.Error`

   Exception raised for errors that are related to the database interface
   rather than the database itself.


.. py:exception:: DatabaseError

   Bases: :class:`py3odb.error.Error`

   Exception raised for errors that are related to the database.


.. py:exception:: InternalError

   Bases: :class:`py3odb.error.DatabaseError`

   Exception raised when the database encounters an internal error,
   e.g. the cursor is not valid anymore, the transaction is out of sync, etc.


.. py:exception:: OperationalError

   Bases: :class:`py3odb.error.DatabaseError`

   Exception raised for errors that are related to the database's operation
   and not necessarily under the control of the programmer, e.g. an unexpected
   disconnect occurs, the data source name is not found, a transaction could
   not be processed, a memory allocation error occured during processing, etc.


.. py:exception:: ProgrammingError

   Bases: :class:`py3odb.error.DatabaseError`

   Exception raised for programming errors, e.g. table not found or already
   exists, syntax error in the SQL statement, wrong number of parameters, etc.


.. py:exception:: IntegrityError

   Bases: :class:`py3odb.error.DatabaseError`

   Exception raised when the relational integrity of the database is affected,
   e.g. a foreign key check fails.


.. py:exception:: DataError

   Bases: :class:`py3odb.error.DatabaseError`

   Exception raised for errors that are due to problems with the processed
   data like division by zero, numeric value out of range, etc.


.. py:exception:: NotSupportedError

   Bases: :class:`py3odb.error.DatabaseError`

   Exception raised in case a method or database API was used wihch is not
   supported by the database, e.g. requesting a rollback() on a connection
   that does not support transactions or has transactions turned off.


