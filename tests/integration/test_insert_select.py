"""Integration test for INSERT and SELECT."""
import pytest
from ..context import py3odb


TEST_DATA = (
    (None, None, None, None),
    (3, 1.2, 'apple', 1),
    (49, 3.14159, 'pie', 2),
    (-12, -0.0003, 'longer_than_8_characters', 3)
)


def test_insert_select(tmpdir):
    """Create a database and then read from it."""
    db_file = tmpdir.join("temp.odb")

    # create a database
    conn = py3odb.connect("")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE t_foo AS (a INTEGER, b REAL, c STRING, d BITFIELD) "
        f"ON '{db_file}'"
    )
    cur.executemany("INSERT INTO t_foo(a,b,c,d) VALUES(?,?,?,?)", TEST_DATA)
    conn.close()

    # read from it
    conn = py3odb.connect(f"{db_file}")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM '{db_file}'")
    data = []
    for row in cur:
        print(f"Fetched row: {row}")
        data.append(row)
    for index, (int_value, real_value, string_value, bitfield_value) in enumerate(TEST_DATA):
        if index == 0:
            assert int_value is None
            assert real_value is None
            assert string_value is None
            assert bitfield_value is None
        else:
            assert int_value == data[index][0]
            assert real_value == pytest.approx(data[index][1])
            assert string_value[:8] == data[index][2]
            assert bitfield_value == data[index][3]
    cur.execute(f"SELECT c FROM '{db_file}' WHERE a=49")
    data = cur.fetchone()
    assert data[0] == "pie"
    conn.close()
