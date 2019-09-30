"""Integration test for INSERT and SELECT."""
import pathlib
from ..context import py3odb


def test_read_sample():
    """Read a sample database."""
    db_file = pathlib.Path(__file__).parent.parent.parent / "resources" / "sample.odb"
    conn = py3odb.connect(f"{db_file}")
    cur = conn.cursor()
    cur.execute(f"SELECT DISTINCT varno@body FROM '{db_file}'")
    varnos = cur.fetchall()
    assert len(varnos) == 3
    assert varnos[0][0] == 162
    assert varnos[1][0] == 241
    assert varnos[2][0] == 7
    conn.close()


def test_fetchmany():
    """Read a database using fetchmany."""
    db_file = pathlib.Path(__file__).parent.parent.parent / "resources" / "sample.odb"
    conn = py3odb.connect(f"{db_file}")
    cur = conn.cursor()
    cur.execute(f"SELECT DISTINCT varno@body FROM '{db_file}'")
    rows = cur.fetchmany(4)
    conn.close()
    assert len(rows) == 3
    assert rows[0]["varno@body"] == 162
    assert rows[1]["varno@body"] == 241
    assert rows[2]["varno@body"] == 7
