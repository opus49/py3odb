:mod:`py3odb.reader`
====================

.. py:module:: py3odb.reader

.. autoapi-nested-parse::

   A context manager that allows iteration of single execution statements.

   >>> with Reader("/path/to/data.odb", "SELECT DISTINCT varno FROM <odb>") as db_reader:
   >>>     for row in db_reader:
   >>>         print(row)



Module Contents
---------------

.. py:class:: Reader(filename, sql_command)

   Class for reading the results of a single SQL query.

   .. attribute:: description
      

      Returns the cursor description if available, otherwise None.


   
   .. method:: __enter__(self)



   
   .. method:: __exit__(self, *args)



   
   .. method:: __iter__(self)



   
   .. method:: __next__(self)




