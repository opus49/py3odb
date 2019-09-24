"""Integration test for INSERT and SELECT."""
import pytest
from ..context import py3odb


TEST_DATA = (
    (0, 1.2, 'apple'),
    (49, 3.14159, 'pie'),
    (-27, -0.0003, 'longer_than_8_characters')
)


def test_insert_select(tmpdir):
    """Create a database and then read from it."""
    db_file = tmpdir.join("temp.odb")

    # create a database
    conn = py3odb.connect("")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE t_foo AS (a INTEGER, b REAL, c STRING) "
        f"ON '{db_file}'"
    )
    cur.executemany("INSERT INTO t_foo(a,b,c) VALUES(?,?,?)", TEST_DATA)
    conn.close()

    # read from it
    conn = py3odb.connect(f"{db_file}")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM '{db_file}'")
    data = []
    for row in cur:
        data.append(row)
    for index, (int_value, real_value, string_value) in enumerate(TEST_DATA):
        assert int_value == data[index][0]
        assert real_value == pytest.approx(data[index][1])
        assert string_value[:8] == data[index][2]
    cur.execute(f"SELECT c FROM '{db_file}' WHERE a=49")
    data = cur.fetchone()
    assert data[0] == "pie"
    conn.close()
