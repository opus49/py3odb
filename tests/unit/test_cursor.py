"""Tests for connection module"""
import pytest
from ..context import py3odb


@pytest.fixture(name="cursor")
def fixture_cursor():
    """Mock cursor for testing."""
    conn = py3odb.connect("")
    cur = conn.cursor()
    yield cur
    conn.close()


class Fetcher:  # pylint: disable=too-few-public-methods
    """Object for handling multiple fetches."""
    def __init__(self, rows_to_fetch):
        self.rows_to_fetch = rows_to_fetch
        self.rows_fetched = 0

    def fetch(self):
        """Mock fetch a value."""
        if self.rows_fetched >= self.rows_to_fetch:
            return None
        self.rows_fetched += 1
        return ("row"),


def test_execute_closed_cursor(cursor):
    """Test that calling execute on a closed cursor raises error."""
    cursor.close()
    with pytest.raises(py3odb.OperationalError):
        cursor.execute("SELECT * FROM foo")


def test_rowcount(cursor):
    """Test that rowcount returns -1"""
    assert cursor.rowcount == -1


def test_fetchone_without_statement(cursor):
    """Test that fetchone raises an error when there is no statement."""
    with pytest.raises(py3odb.ProgrammingError):
        cursor.fetchone()


def test_fetchmany_default_size(cursor, monkeypatch):
    """Test fetchmany without default size."""
    def mock_fetchone(*args):  # pylint: disable=missing-docstring,unused-argument
        return ("row"),
    monkeypatch.setattr(py3odb.cursor.Cursor, "fetchone", mock_fetchone)
    rows = cursor.fetchmany()
    assert len(rows) == cursor.arraysize


def test_fetchmany_with_size(cursor, monkeypatch):
    """Test fetchmany without a provided size."""
    def mock_fetchone(*args):  # pylint: disable=missing-docstring,unused-argument
        return ("row"),
    monkeypatch.setattr(py3odb.cursor.Cursor, "fetchone", mock_fetchone)
    rows = cursor.fetchmany(5)
    assert len(rows) == 5


def test_fetchmany_without_rows(cursor, monkeypatch):
    """Test fetchmany when the remaining rows is fewer than arraysize."""
    def mock_fetchone(*args):  # pylint: disable=missing-docstring,unused-argument
        return None
    monkeypatch.setattr(py3odb.cursor.Cursor, "fetchone", mock_fetchone)
    rows = cursor.fetchmany()
    assert not rows


def test_fetchall(cursor, monkeypatch):
    """Test fetchall."""
    rows_to_fetch = 3
    fetcher = Fetcher(rows_to_fetch)
    monkeypatch.setattr(py3odb.cursor.Cursor, "fetchone", fetcher.fetch)
    rows = cursor.fetchall()
    assert len(rows) == rows_to_fetch


def test_finalize_warning(cursor, monkeypatch):
    """Test that a finalize error causes a warning."""
    def mock_odbql_finalize(*args):  # pylint: disable=missing-docstring,unused-argument
        return py3odb.odbql.ODBQL_ERROR
    monkeypatch.setattr("py3odb.odbql.odbql_finalize", mock_odbql_finalize)
    cursor.execute("CREATE TABLE t_foo AS (x INTEGER)")
    with pytest.warns(RuntimeWarning):
        cursor.finalize()


def test_setinputsizes_not_supported(cursor):
    """Test that setinputsizes raises NotSupportedError."""
    with pytest.raises(py3odb.NotSupportedError):
        cursor.setinputsizes(None)


def test_setoutputsize_not_supported(cursor):
    """Test that setoutputsize raises NotSupportedError."""
    with pytest.raises(py3odb.NotSupportedError):
        cursor.setoutputsize()


def test_description_defaults_none(cursor):
    """Test that the cursor description defaults to none."""
    assert cursor.description is None


def test_invalid_bind_parameter(cursor, tmpdir):
    """Test that passing an invalid type as a bind parameter raises an error."""
    db_file = tmpdir.join("invalid_bind.odb")
    cursor.execute(f"CREATE TABLE t_foo AS (x INTEGER) ON '{db_file}'")
    invalid_parameter = {"key": "value"}
    with pytest.raises(py3odb.ProgrammingError):
        cursor.execute("INSERT INTO t_foo(x) VALUES(?)", (invalid_parameter,))


def test_bind_failure(cursor, tmpdir, monkeypatch):
    """Test that a bind failure raises an error."""
    def mock_odbql_bind(*args):  # pylint: disable=missing-docstring,unused-argument
        return py3odb.odbql.ODBQL_ERROR
    monkeypatch.setattr("py3odb.odbql.odbql_bind_null", mock_odbql_bind)
    db_file = tmpdir.join("invalid_bind.odb")
    cursor.execute(f"CREATE TABLE t_foo AS (x INTEGER) ON '{db_file}'")
    with pytest.raises(py3odb.ProgrammingError):
        cursor.execute("INSERT INTO t_foo(x) VALUES(?)", (None,))


def test_execute_prep_failure(cursor, tmpdir, monkeypatch):
    """Test that execute handles a prepare_statement failure."""
    def mock_odbql_prep(*args):  # pylint: disable=missing-docstring,unused-argument
        return py3odb.odbql.ODBQL_ERROR

    def mock_odbql_errmsg(*args):  # pylint: disable=missing-docstring,unused-argument
        return b""
    monkeypatch.setattr("py3odb.odbql.odbql_prepare_v2", mock_odbql_prep)
    monkeypatch.setattr("py3odb.odbql.odbql_errmsg", mock_odbql_errmsg)
    db_file = tmpdir.join("invalid_bind.odb")
    with pytest.raises(py3odb.ProgrammingError):
        cursor.execute(f"CREATE TABLE t_foo AS (x INTEGER) ON '{db_file}'")
