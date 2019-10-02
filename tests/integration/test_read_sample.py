"""Integration test for INSERT and SELECT."""
from ..context import py3odb


def test_read_sample(sample_odb):
    """Read a sample database."""
    conn = py3odb.connect(sample_odb)
    cur = conn.cursor()
    cur.execute(f"SELECT DISTINCT varno@body FROM '{sample_odb}'")
    varnos = cur.fetchall()
    assert len(varnos) == 3
    assert varnos[0][0] == 162
    assert varnos[1][0] == 241
    assert varnos[2][0] == 7
    conn.close()


def test_fetchmany(sample_odb):
    """Read a database using fetchmany."""
    conn = py3odb.connect(sample_odb)
    cur = conn.cursor()
    cur.execute(f"SELECT DISTINCT varno@body FROM <odb>;")
    rows = cur.fetchmany(4)
    conn.close()
    assert len(rows) == 3
    assert rows[0]["varno@body"] == 162
    assert rows[1]["varno@body"] == 241
    assert rows[2]["varno@body"] == 7
