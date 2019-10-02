:mod:`py3odb.cursor`
====================

.. py:module:: py3odb.cursor

.. autoapi-nested-parse::

   Cursor object



Module Contents
---------------

.. py:class:: Cursor(connection)

   A database cursor which is used to manage the context of a fetch operation.
   Cursors created from the same connection are not isolated.

   .. attribute:: description
      

      Read-only attribute that is a sequence of 7-item sequences.  This class
      uses a tuple of tuples to describe column results.  The tuple elements
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

      The type_code can be interpreted by comparing it to the Type Objects.


   .. attribute:: rowcount
      

      Read-only attribute specifies the number of rows that the last execute
      produced.  The attribute is -1 in case no execute has been performed on
      the cursor or the rowcount of the last operation cannot be determined.


   
   .. method:: __iter__(self)



   
   .. method:: __next__(self)



   
   .. method:: _bind_parameters(self, parameters)

      Bind a sequence of parameters to an SQL statement.



   
   .. staticmethod:: _column_info(name, column_type)

      Shorthand method for filling out the 7-item description tuples.



   
   .. method:: _get_column(self, index)

      Get the column value for the current row at the given index.



   
   .. method:: _populate_metadata(self)

      Generate the metadata for the most recent column results.



   
   .. method:: _prepare_statement(self, operation)

      Prepare a database operation.



   
   .. method:: close(self)

      Close the cursor now.  The cursor will be unusable from this point
      forward and an exception will be raised if any operation is attempted.



   
   .. method:: execute(self, operation, parameters=None)

      Prepare and execute a database operation (query or command).
      ODBQL only supports parameterized INSERT statements and does not
      support parameterization of SELECT statements.  Parameters must be
      a sequence and will be bound to variables in the operation.



   
   .. method:: executemany(self, operation, seq_of_parameters)

      Prepare a database operation (query or command) and then execute
      it against all parameter sequences found in seq_of_parameters.



   
   .. method:: fetchone(self)

      Fetch the next row of a query result set, returning a single sequence,
      or None when no more data is available.  A ProgrammingError is raised
      if the previous call to execute did not produce any result set or no
      call was issued yet.  For py3odb, the fetch returns a Row object.



   
   .. method:: fetchmany(self, size=None)

      Fetch the next set of rows of a query result, returning a sequence
      of sequences (e.g. a list of tuples).  An empty sequence is returned
      when no more rows are available.



   
   .. method:: fetchall(self)

      Fetch all (remaining) rows of a query result, returning them as a sequence
      of sequences (i.e. a list of tuples).



   
   .. method:: finalize(self)

      Destroy the prepared statement object.



   
   .. staticmethod:: setinputsizes(sizes)

      Per PEP 249:  Implementations are free to have this method do
      nothing and users are free to not use it.



   
   .. staticmethod:: setoutputsize()

      Per PEP 249:  Implementations are free to have this method do
      nothing and users are free to not use it.




