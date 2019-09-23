[![Build Status](https://travis-ci.org/opus49/py3odb.svg?branch=master)](https://travis-ci.org/opus49/py3odb)
[![Coverage Status](https://coveralls.io/repos/github/opus49/py3odb/badge.svg?branch=master)](https://coveralls.io/github/opus49/py3odb?branch=master)

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

## Notes
For now this is a list of things I want to remember:
* odbql only supports 8 character strings in its TEXT functions
* only the last INSERT takes for some reason
* you can't open an existing database and do an insert
* since there is no real bulk retrieval, does a fetch iterator really make sense?


## Acknowledgments
Based on the Python 2 version provided by [ECMWF](https://confluence.ecmwf.int/display/ODBAPI).


## Links
* https://www.python.org/dev/peps/pep-0249
* https://confluence.ecmwf.int/display/ODBAPI
