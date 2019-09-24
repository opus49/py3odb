"""Integration tests INSERT with NULL values."""
from ..context import py3odb


TEST_DATA = (
    (None, None, None),
    (0, 1.2, 'apple'),
    (49, 3.14159, 'pie'),
    (-27, -0.0003, 'longer_than_8_characters')
)


def test_insert_with_nulls(tmpdir):
    """Create a database and then read from it using iterator."""
    db_file = tmpdir.join("insert_with_nulls.odb")

    # create a database
    conn = py3odb.connect("")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE t_foo AS (a INTEGER, b REAL, c STRING) "
        f"ON '{db_file}'"
    )
    cur.executemany("INSERT INTO t_foo(a,b,c) VALUES(?,?,?)", TEST_DATA)
    conn.close()
