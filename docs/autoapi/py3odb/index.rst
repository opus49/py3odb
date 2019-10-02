:mod:`py3odb`
=============

.. py:module:: py3odb

.. autoapi-nested-parse::

   Python 3.6+ compatible interface to ECMWF's ODB API



Subpackages
-----------
.. toctree::
   :titlesonly:
   :maxdepth: 3

   cli/index.rst
   constants/index.rst


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   connection/index.rst
   cursor/index.rst
   error/index.rst
   odbql/index.rst
   reader/index.rst
   row/index.rst
   util/index.rst


Package Contents
----------------

.. function:: connect(filename)

   Creates a connection to the database.


.. py:class:: Connection(filename)

   A connection to the database.

   .. attribute:: database
      

      Reference to the underlying odbql database object.


   .. attribute:: is_connected
      

      Read-only attribute for the the connection status.


   .. attribute:: filename
      

      The filename representing the connected database.


   
   .. staticmethod:: _open(filename)

      Opens a connection to a database and returns an odbql object.



   
   .. method:: close(self)

      Close the connection now.



   
   .. staticmethod:: commit()

      Commit any pending transaction to the database.



   
   .. staticmethod:: rollback()

      Roll back to the start of any pending transaction.



   
   .. method:: cursor(self)

      Return a new Cursor object using the connection.




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


.. py:class:: Reader(filename, sql_command)

   Class for reading the results of a single SQL query.

   .. attribute:: description
      

      Returns the cursor description if available, otherwise None.


   
   .. method:: __enter__(self)



   
   .. method:: __exit__(self, *args)



   
   .. method:: __iter__(self)



   
   .. method:: __next__(self)




