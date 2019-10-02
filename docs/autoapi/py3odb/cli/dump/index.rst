:mod:`py3odb.cli.dump`
======================

.. py:module:: py3odb.cli.dump

.. autoapi-nested-parse::

   Module for the dump command.



Module Contents
---------------

.. py:class:: DumpCommand

   Bases: :class:`py3odb.cli.Command`

   The dump command.

   .. attribute:: help_text
      :annotation: = Dump information about the ODB2 file (e.g. column names).

      

   .. attribute:: description
      

      Describes the dump command.


   
   .. staticmethod:: _get_column_data(filename)

      Retrieve a dictionary of column names and types.



   
   .. staticmethod:: _get_varno_data(filename)

      Retrieve a sorted list of tuples containing varno code, name, desc.



   
   .. method:: add_arguments(self)



   
   .. method:: command(self, args)

      Run the dump command.



   
   .. method:: print_columns(self, filename, verbose=False)

      Print the columns from an ODB2 file.



   
   .. method:: print_varnos(self, filename, verbose=False)

      Print a list of varnos from an ODB2 file.




