:mod:`py3odb.cli`
=================

.. py:module:: py3odb.cli

.. autoapi-nested-parse::

   Module to support the Command Line Interface (CLI)



Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   command/index.rst
   dump/index.rst
   geopoints/index.rst
   main/index.rst
   query/index.rst


Package Contents
----------------

.. py:class:: Command(subparsers)

   Bases: :class:`abc.ABC`

   Abstract class that defines a command for argument parsing.

   .. attribute:: help_text
      

      

   .. attribute:: name
      

      The name of this command.


   .. attribute:: description
      

      The description to print before help text.


   
   .. method:: add_arguments(self)

      Add the arguments specific to this command.



   
   .. method:: command(self, args)

      The underlying function that is called when a command is selected.




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




