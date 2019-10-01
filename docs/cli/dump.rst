Dump
====

The dump command provides a way to view specific information about an ODB2 file from the command line.  It will provide ``columns`` or ``varno`` based on the switch:

.. code-block:: bash

    usage: py3odb dump [-h] [-c] [-v] [-vv] filename

    Dump information about the ODB2 file (e.g. column names).

    positional arguments:
      filename        The ODB2 filename.

    optional arguments:
      -h, --help      show this help message and exit
      -c, --columns   Print the columns.
      -v, --varno     Print the varnos.
      -vv, --verbose  Print full details.


Example usage:

.. code-block:: bash

    $ py3odb dump -c -vv sample.odb
    ---------------------------------------------------
    name                                    type
    ---------------------------------------------------
    air_quality_station_name_1@conv         TEXT
    aircraft_airframe_code@conv             TEXT
    aircraft_data_relay_system@conv         INTEGER
    aircraft_geomagnetic_deviation@conv     FLOAT
    ...


.. code-block:: bash

    $ py3odb dump --varno --verbose sample.odb
    --------------------------------------------------------------------------------
    name                code  description
    --------------------------------------------------------------------------------
    bend_angle           162  radio occultation bending angle
    mean_freq            241  GPSRO mean frequency
    q                      7  specific humidity (q)
