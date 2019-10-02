:mod:`py3odb.cli.query`
=======================

.. py:module:: py3odb.cli.query

.. autoapi-nested-parse::

   Module for the query command.



Module Contents
---------------

.. py:class:: QueryCommand

   Bases: :class:`py3odb.cli.Command`

   The query command.

   .. attribute:: help_text
      :annotation: = Execute an SQL-like query against an ODB2 file.

      

   .. attribute:: desc_text
      

      

   .. attribute:: description
      

      Describes the query command.


   
   .. method:: add_arguments(self)

      Add the arguments specific to this command.



   
   .. method:: command(self, args)

      Run the query command.




