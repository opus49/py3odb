=====
Query
=====

The query command provides a way to run SQL commands directly on an ODB2 file from the command line.  Keep in mind that ODB2 is not a relational database in the traditional sense.  Commands are limited to simple SELECT statements.  The \<odb> substitution tag will work with the query command.


Usage
-----
.. code-block:: bash

    usage: py3odb query [-h] filename sql_command

    Execute an SQL-like query against an ODB2 file.
    You can replace the filename reference in the SQL command with <odb>.

    Examples:
        $ py3odb query foo.odb "SELECT DISTINCT varno FROM 'foo.odb'"
        $ py3odb query foo.odb "SELECT lat,lon,obsvalue FROM <odb>"

    positional arguments:
      filename     The ODB2 filename.
      sql_command  The SQL commmand to execute.  Use <odb> to reference the filename.

    optional arguments:
      -h, --help   show this help message and exit


Examples
--------

.. code-block:: bash

    $ py3odb query sample.odb "SELECT DISTINCT date@hdr FROM <odb>"
    (20181213,)


.. code-block:: bash

    $ py3odb query sample.odb "SELECT varno,lat,lon,obsvalue FROM <odb>"
    (162, -74.678, -35.619, 0.013708969578146935)
    (241, -74.678, -35.619, None)
    (7, -74.678, -35.619, None)
    ...
