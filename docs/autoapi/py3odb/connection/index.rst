:mod:`py3odb.connection`
========================

.. py:module:: py3odb.connection

.. autoapi-nested-parse::

   Connection object and connect function



Module Contents
---------------

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




