# py3odb
Python 3.6+ compatible interface to ECMWF's ODB API


## Installation
TBD


## Usage
py3odb follows the [Python Database API Specification](https://www.python.org/dev/peps/pep-0249):

    import py3odb
    conn = py3odb.connect('foo.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM "foo.db"')
    data = cur.fetchmany()

See [PEP 249](https://www.python.org/dev/peps/pep-0249) for more details.


## Acknowledgments
Based on the Python 2 version provided by [ECMWF](https://confluence.ecmwf.int/display/ODBAPI).


## Links
* https://www.python.org/dev/peps/pep-0249
* https://confluence.ecmwf.int/display/ODBAPI
