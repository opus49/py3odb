=========
Geopoints
=========

The geopoints command generates output compatible with `Metview`_.  The user supplies a single column (e.g. obsvalue\@body) and varno (name or code).  Currently the level is set to zero regardless of the contents of the odb file.  *This command is experimental and not guaranteed to work.*

Usage
-----
.. code-block:: bash

    usage: py3odb geopoints [-h] -c COLUMN -v VARNO [-w WHERE] filename

    Generate a standard 6-column geopoints file for Metview.
    You must supply the filename, column, and varno.  You may use the
    varno name or code.

    Examples:
        $ py3odb geopoints sample.odb -c obsvalue@body -v 39
        $ py3odb geopoints sample.odb -c bgvalue -v t2m

    See https://apps.ecmwf.int/odbgov/varno/

    positional arguments:
      filename              The ODB2 filename.

    optional arguments:
      -h, --help            show this help message and exit
      -c COLUMN, --column COLUMN
                            The column to include (e.g. obsvalue@body).
      -v VARNO, --varno VARNO
                            The varno to include.  May be either name or code.
      -w WHERE, --where WHERE
                            Adds a conditional to the SQL query.


Examples
--------
.. code-block:: bash

    $ py3odb geopoints sample.odb -c obsvalue -v t2m
    #GEO
    VARNO = 39
    COLUMN = obsvalue@body
      lat       lon     lvl   date      time      value
    #DATA
      57.183     9.950   0   20181213   0600    272.671814
      57.100     9.850   0   20181213   0600    273.486420
      57.733    10.633   0   20181213   0600    274.932434
      56.933     8.633   0   20181213   0600    273.601471
      57.383    10.333   0   20181213   0600    273.796997
      ...


.. code-block:: bash

    $ py3odb geopoints sample.odb -c obsvalue -v t2m -w "lon > 9 AND lon < 10"
    #GEO
    VARNO = 39
    COLUMN = obsvalue@body
      lat       lon     lvl   date      time      value
    #DATA
      57.183     9.950   0   20181213   0600    272.671814
      57.100     9.850   0   20181213   0600    273.486420
      ...


References
----------
- ODB Database varnos: https://apps.ecmwf.int/odbgov/varno/
- ODB Database columns: https://apps.ecmwf.int/odbgov/column/

.. _Metview: https://confluence.ecmwf.int/display/METV
