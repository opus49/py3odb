:mod:`py3odb.cli.geopoints`
===========================

.. py:module:: py3odb.cli.geopoints

.. autoapi-nested-parse::

   Module for the geopoints command.



Module Contents
---------------

.. py:class:: GeopointsCommand

   Bases: :class:`py3odb.cli.Command`

   The geopoints command.

   .. attribute:: help_text
      :annotation: = Generate a standard 6-column geopoints file for Metview.

      

   .. attribute:: desc_text
      

      

   .. attribute:: description
      

      Describes the geopoints command.


   
   .. method:: add_arguments(self)



   
   .. method:: command(self, args)

      Run the geopoints command.




.. py:class:: GeopointsRunner(filename, varno, column)

   Class for running geopoints file generation.

   
   .. staticmethod:: error(message)

      Handle fatal errors.



   
   .. method:: generate_header(self)

      Generate the header for the geopoints file.



   
   .. method:: generate_sql_command(self)

      Generate the SQL command from the varno and column.



   
   .. method:: run(self)

      Query the database and return a list of lines in geopoints format.



   
   .. staticmethod:: _parse_antime(antime)

      Convert antime to format geopoints expects.



   
   .. method:: _validate_column(self, column)

      Make sure the column exists and correct if necessary.



   
   .. method:: _validate_varno(self, raw_varno)

      Convert the user supplied varno into a usable value.




