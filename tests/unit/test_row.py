"""Tests for row module"""
import pytest
from ..context import py3odb


@pytest.fixture(name="test_row")
def test_row_fixture():
    """Set up a test row."""
    test_data = {
        "apples": -49,
        "pie": 3.14159,
        "name": "foo",
        "fstogive": None
    }
    return py3odb.row.Row(test_data)


def test_row_immutable():
    """Test that the row is immutable."""
    immutable_row = py3odb.row.Row()
    with pytest.raises(TypeError):
        immutable_row["key"] = 0  # pylint: disable=unsupported-assignment-operation
    with pytest.raises(TypeError):
        immutable_row[0] = 0  # pylint: disable=unsupported-assignment-operation


def test_row_get_item(test_row):
    """Test get_item method."""
    assert test_row[0] == -49
    assert test_row["pie"] == 3.14159
    assert test_row["name"] == "foo"
    assert test_row["fstogive"] is None
    assert test_row.get("missing", None) is None


def test_row_repr(test_row):
    """Test repr method."""
    assert repr(test_row) == "Row({'apples': -49, 'pie': 3.14159, 'name': 'foo', 'fstogive': None})"


def test_row_str(test_row):
    """Test str method."""
    assert str(test_row) == "(-49, 3.14159, 'foo', None)"


def test_len(test_row):
    """Test len method."""
    assert len(test_row) == 4
    empty_row = py3odb.row.Row()
    assert not empty_row


def test_iterator(test_row):
    """Test row iteration."""
    expected_values = [-49, 3.14159, 'foo', None]
    for index, value in enumerate(test_row):
        assert value == expected_values[index]
