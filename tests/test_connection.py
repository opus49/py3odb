"""Tests for connection module"""
import pytest
from .context import py3odb


def test_connect_empty():
    """Test the connect function without passing an odb filename."""
    conn = py3odb.connect("")
    assert conn.is_connected
    conn.close()
    assert not conn.is_connected


def test_connect_fails():
    """Test the connect function to an invalid odb filename."""
    with pytest.raises(py3odb.InterfaceError):
        py3odb.connect("invalid_filename")
