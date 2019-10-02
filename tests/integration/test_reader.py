"""Integration test for Reader context manager."""
from ..context import py3odb


def test_reader(sample_odb):
    """Use the Reader context manager to read an odb file."""
    varnos = []
    with py3odb.Reader(sample_odb, "SELECT DISTINCT varno@body FROM <odb>") as odb_reader:
        assert odb_reader.description[0][0] == "varno@body"
        for row in odb_reader:
            varnos.append(row["varno@body"])
    assert len(varnos) == 3
    assert varnos[0] == 162
    assert varnos[1] == 241
    assert varnos[2] == 7
