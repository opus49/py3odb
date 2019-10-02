:mod:`py3odb.constants`
=======================

.. py:module:: py3odb.constants

.. autoapi-nested-parse::

   Module for storing constant variables and static classes.



Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   varno/index.rst


Package Contents
----------------

.. py:class:: Varno

   Static class for looking up varno information.

   
   .. staticmethod:: get_name(code)

      Get the varno name for the given code.



   
   .. staticmethod:: get_code(name)

      Get the varno code given the name.



   
   .. staticmethod:: get_desc(name)

      Get the description of the given varno.




.. py:class:: ColumnType

   Bases: :class:`enum.Enum`

   Constant values for the various column types.

   .. attribute:: INTEGER
      :annotation: = 1

      

   .. attribute:: FLOAT
      :annotation: = 2

      

   .. attribute:: TEXT
      :annotation: = 3

      

   .. attribute:: BLOB
      :annotation: = 4

      

   .. attribute:: NULL
      :annotation: = 5

      

   .. attribute:: BITFIELD
      :annotation: = 6

      


