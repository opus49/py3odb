:mod:`py3odb.odbql`
===================

.. py:module:: py3odb.odbql

.. autoapi-nested-parse::

   Use ctypes to load libOdb.so and access symbols



Module Contents
---------------

.. data:: _LIB
   

   

.. data:: _ODBQL
   

   

.. data:: restype
   

   

.. data:: restype
   

   

.. data:: restype
   

   

.. data:: restype
   

   

.. data:: ODBQL_OK
   :annotation: = 0

   

.. data:: ODBQL_ERROR
   :annotation: = 1

   

.. data:: ODBQL_BUSY
   :annotation: = 5

   

.. data:: ODBQL_ROW
   :annotation: = 100

   

.. data:: ODBQL_DONE
   :annotation: = 101

   

.. data:: ODBQL_METADATA_CHANGED
   :annotation: = 102

   

.. data:: ODBQL_STATIC
   

   

.. function:: odbql_bind_double(*args)

   Bind double (Python float) values to prepared statements.
   ODBQL_API int odbql_bind_double(odbql_stmt*, int, double)


.. function:: odbql_bind_int(*args)

   Bind integer values to prepared statements.
   ODBQL_API int odbql_bind_int(odbql_stmt*, int, int)


.. function:: odbql_bind_null(*args)

   Bind NULL values to prepared statements.
   ODBQL_API int odbql_bind_null(odbql_stmt*, int)


.. function:: odbql_bind_text(*args)

   Bind string values to prepared statements.
   ODBQL_API int odbql_bind_text(odbql_stmt*, int, const char*, int, void(*), (void*))


.. function:: odbql_close(*args)

   Destroys odbql object.
   ODBQL_API int odbql_close(odbql*);


.. function:: odbql_column_count(*args)

   Returns the number of columns in the result set returned by the prepared
   statement.  Returns zero if pStmt is an SQL statemement that does not
   return data (e.g. UPDATE).
   ODBQL_API int odbql_column_count(odbql_stmt *pStmt);


.. function:: odbql_column_name(*args)

   Returns the name assigned to a particular column in the result set
   of a SELECT statement. N is the column number (starting at zero).
   ODBQL_API const char * odbql_column_name(odbql_stmt*, int N);


.. function:: odbql_column_text(*args)

   Returns the referenced column as text.
   ODBQL_API unsigned char * odbql_column_text(odbql_stmt*, int iCol);


.. function:: odbql_column_type(*args)

   Returns the datatype code for the initial data type of the result column.
   ODBQL_API int odbql_column_type(odbql_stmt*, int iCol);


.. function:: odbql_column_value(*args)

   Returns the odbql_value object for the column.
   ODBQL_API odbql_value odbql_column_value(odbql_stmt*, int iCol);


.. function:: odbql_errmsg(*args)

   If the most recent API call was unsuccessful, odbql_errmsg will return
   English-language text that describes the error.  Requires that
   odbql_errmsg.restype be set to ctypes.c_char_p.
   ODBQL_API const char * odbql_errmsg(odbql*);


.. function:: odbql_finalize(*args)

   Destroys a prepared statement object.
   ODBQL_API int odbql_finalize(odbql_stmt *pStmt);


.. function:: odbql_open(*args)

   Creates odbql object.
   ODBQL_API int odbql_open(const char *filename, odbql **ppDb);


.. function:: odbql_prepare_v2(*args)

   Compiles SQL query into byte-code program.
   ODBQL_API int odbql_prepare_v2(
       odbql *db,            /* Database handle */
       const char *zSql,     /* SQL statement, UTF-8 encoded */
       int nByte,            /* Maximum length of zSql in bytes. */
       odbql_stmt **ppStmt,  /* OUT: Statement handle */
       const char **pzTail   /* OUT: Pointer to unused portion of zSql */


.. function:: odbql_step(*args)

   Evaluates an SQL statement.  After a statement has been prepared, this
   function must be called one or more times to evaluate the statement.
   ODBQL_DONE means that the statement has finished executing successfully.
   obql_step() should not be called again without first calling odbql_reset().
   If the SQL statement returns any data, then ODBQL_ROW is returned each
   time a new row of data is ready for processing by the caller.  The values
   may be accessed by using the column access functions.
   ODBQL_API int odbql_step(odbql_stmt*);


.. function:: odbql_value_double(*args)

   Converts an odbql_value object into a double.
   ODBQL_API double odbql_value_double(odbql_value*);


.. function:: odbql_value_int(*args)

   Converts an odbql_value object into an integer.
   ODBQL_API int odbql_value_int(odbql_value*);


