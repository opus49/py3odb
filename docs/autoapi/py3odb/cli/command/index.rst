:mod:`py3odb.cli.command`
=========================

.. py:module:: py3odb.cli.command

.. autoapi-nested-parse::

   Module for abstract Command class to support argument parsing.



Module Contents
---------------

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




