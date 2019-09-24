"""Integration tests for INSERT using BITFIELD field."""
from ..context import py3odb


TEST_DATA = (
    (0, 1.2, 'apple', 5),
    (49, 3.14159, 'pie', 10),
    (-27, -0.0003, 'longer_than_8_characters', 15)
)


def test_insert_with_bitfield(tmpdir):
    """Create a database and insert."""
    db_file = tmpdir.join("insert_with_bitfield.odb")

    # create a database
    conn = py3odb.connect("")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE t_foo AS (a INTEGER, b REAL, c STRING, d BITFIELD) "
        f"ON '{db_file}'"
    )
    cur.executemany("INSERT INTO t_foo(a,b,c,d) VALUES(?,?,?,?)", TEST_DATA)
    conn.close()
