"""Tests for connection module"""
import pytest
from ..context import py3odb


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


def test_close_closes_cursors():
    """Test that the close method closes all cursors."""
    conn = py3odb.connect("")
    cursors = []
    for _ in range(3):
        cursors.append(conn.cursor())
    conn.close()
    for cursor in cursors:
        with pytest.raises(py3odb.OperationalError):
            cursor.execute("CREATE TABLE t_foo AS (x INTEGER)")


def test_close_handles_odbql_busy(monkeypatch):
    """Test that the close method handles ODBQL_BUSY."""
    def mock_odbql_close(connection):  # pylint: disable=missing-docstring,unused-argument
        return py3odb.odbql.ODBQL_BUSY
    monkeypatch.setattr("py3odb.odbql.odbql_close", mock_odbql_close)
    conn = py3odb.connect("")
    with pytest.warns(RuntimeWarning):
        conn.close()
    assert conn.is_connected


def test_close_handles_odbql_error(monkeypatch):
    """Test that the close method handles ODBQL_ERROR."""
    def mock_odbql_close(connection):  # pylint: disable=missing-docstring,unused-argument
        return py3odb.odbql.ODBQL_ERROR
    monkeypatch.setattr("py3odb.odbql.odbql_close", mock_odbql_close)
    conn = py3odb.connect("")
    with pytest.warns(RuntimeWarning):
        conn.close()
    assert conn.is_connected


def test_rollback_raises_error():
    """Test that the rollback method raises a NotSupportedError."""
    conn = py3odb.connect("")
    with pytest.raises(py3odb.NotSupportedError):
        conn.rollback()


def test_cursor_closed_connection():
    """
    Test that trying to use the cursor method on a close connection
    raises an OperationalError.
    """
    conn = py3odb.connect("")
    conn.close()
    with pytest.raises(py3odb.OperationalError):
        conn.cursor()


def test_commit_raises_error():
    """Test that the commit method raises a NotSupportedError."""
    conn = py3odb.connect("")
    with pytest.raises(py3odb.NotSupportedError):
        conn.commit()
