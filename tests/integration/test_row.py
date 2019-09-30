"""Integration test for Row object."""
import pathlib
from ..context import py3odb


def test_row():
    """Test the iteration capability of the Row object on real data."""
    db_file = pathlib.Path(__file__).parent.parent.parent / "resources" / "sample.odb"
    with py3odb.Reader(str(db_file), "SELECT varno,lat,lon,obsvalue FROM <odb>") as odb_reader:
        for row in odb_reader:
            assert len(row) == 4
            assert repr(row) == \
                "Row({'varno@body': 162, 'lat@hdr': -74.678, " \
                "'lon@hdr': -35.619, 'obsvalue@body': None})"
            for index, value in enumerate(row):
                if index == 0:
                    assert value == 162
                elif index == 1:
                    assert value == -74.678
                elif index == 2:
                    assert value == -35.619
                else:
                    assert value is None
            break
