"""Integration tests for the py3odb module."""
import pytest
from ..context import py3odb

TEST_DATA = (
    (0, 1.2, 'apple'),
    (49, 3.14159, 'pie'),
    (-27, -0.0003, 'longer_than_8_characters')
)


def test_database(tmpdir):
    """Create a database and then read from it."""
    db_file = tmpdir.join("test.odb")
    conn = py3odb.connect("")
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE t_foo AS (x INTEGER, y REAL, z STRING) ON '{db_file}'")
    cur.executemany(
        "INSERT INTO t_foo(x,y,z) VALUES(?,?,?)",
        (
            (0, 1.2, 'apple'),
            (49, 3.14159, 'pie'),
            (-27, -0.0003, 'longer_than_8_characters')
        )
    )
    conn.close()

    conn = py3odb.connect(f"{db_file}")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM '{db_file}'")
    data = cur.fetchall()
    conn.close()

    for index, (int_value, real_value, string_value) in enumerate(TEST_DATA):
        assert int_value == data[index][0]
        assert real_value == pytest.approx(data[index][1])
        assert string_value[:8] == data[index][2]
