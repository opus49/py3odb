"""Tests for connection module"""
import ctypes
import pytest
from ..context import py3odb


@pytest.fixture(name="cursor")
def fixture_cursor():
    """Mock cursor for testing."""
    conn = py3odb.connect("")
    cur = conn.cursor()
    yield cur
    conn.close()


class MockFetcher:  # pylint: disable=too-few-public-methods
    """Mock object for handling multiple fetches."""
    def __init__(self, rows_to_fetch):
        self.rows_to_fetch = rows_to_fetch
        self.rows_fetched = 0

    def fetch(self):
        """Mock fetch a value."""
        if self.rows_fetched >= self.rows_to_fetch:
            return None
        if self.rows_fetched == 0:
            value = 1
        elif self.rows_fetched == 1:
            value = "foo"
        elif self.rows_fetched == 2:
            value = 3.14159
        else:
            value = None
        self.rows_fetched += 1
        return py3odb.row.Row({"key": value})


class MockODBQL:
    """Mock object for handling odbql calls."""
    def __init__(self):
        self.calls = []

    def odbql_bind_null(self, *args):
        """Mock odbql_bind_null."""
        self.calls.append(("null", *args))
        return 0

    def odbql_bind_text(self, *args):
        """Mock odbql_bind_text."""
        self.calls.append(("text", *args))
        return 0

    def odbql_bind_int(self, *args):
        """Mock odbql_bind_int."""
        self.calls.append(("int", *args))
        return 0

    def odbql_bind_double(self, *args):
        """Mock odbql_bind_double."""
        self.calls.append(("double", *args))
        return 0


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
    def mock_fetchone(*args):
        """mock fetchone"""
        return ("row"),
    monkeypatch.setattr(py3odb.cursor.Cursor, "fetchone", mock_fetchone)
    rows = cursor.fetchmany()
    assert len(rows) == cursor.arraysize


def test_fetchmany_with_size(cursor, monkeypatch):
    """Test fetchmany without a provided size."""
    def mock_fetchone(*args):
        """mock fetchone"""
        return ("row"),
    monkeypatch.setattr(py3odb.cursor.Cursor, "fetchone", mock_fetchone)
    rows = cursor.fetchmany(5)
    assert len(rows) == 5


def test_fetchmany_without_rows(cursor, monkeypatch):
    """Test fetchmany when the remaining rows is fewer than arraysize."""
    def mock_fetchone(*args):
        """mock fetchone"""
        return None
    monkeypatch.setattr(py3odb.cursor.Cursor, "fetchone", mock_fetchone)
    rows = cursor.fetchmany()
    assert not rows


def test_fetchall(cursor, monkeypatch):
    """Test fetchall."""
    rows_to_fetch = 4
    fetcher = MockFetcher(rows_to_fetch)
    monkeypatch.setattr(py3odb.cursor.Cursor, "fetchone", fetcher.fetch)
    rows = cursor.fetchall()
    assert len(rows) == rows_to_fetch
    assert rows[0][0] == 1
    assert rows[1]["key"] == "foo"
    assert rows[2]["key"] == 3.14159
    assert rows[3]["key"] is None


def test_finalize_warning(cursor, monkeypatch):
    """Test that a finalize error causes a warning."""
    def mock_odbql_finalize(*args):
        """ mock odbql_finalize"""
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
    def mock_odbql_bind(*args):
        """mock odbql_bind"""
        return py3odb.odbql.ODBQL_ERROR
    monkeypatch.setattr("py3odb.odbql.odbql_bind_null", mock_odbql_bind)
    db_file = tmpdir.join("invalid_bind.odb")
    cursor.execute(f"CREATE TABLE t_foo AS (x INTEGER) ON '{db_file}'")
    with pytest.raises(py3odb.ProgrammingError):
        cursor.execute("INSERT INTO t_foo(x) VALUES(?)", (None,))


def test_execute_prep_failure(cursor, tmpdir, monkeypatch):
    """Test that execute handles a prepare_statement failure."""
    def mock_odbql_prep(*args):
        """mock odbql_prepare_v2"""
        return py3odb.odbql.ODBQL_ERROR

    def mock_odbql_errmsg(*args):
        """mock odbql_errmsg"""
        return b""
    monkeypatch.setattr("py3odb.odbql.odbql_prepare_v2", mock_odbql_prep)
    monkeypatch.setattr("py3odb.odbql.odbql_errmsg", mock_odbql_errmsg)
    db_file = tmpdir.join("invalid_bind.odb")
    with pytest.raises(py3odb.ProgrammingError):
        cursor.execute(f"CREATE TABLE t_foo AS (x INTEGER) ON '{db_file}'")


def test_iteration(cursor, monkeypatch):
    """Test cursor iteration."""
    rows_to_fetch = 4
    fetcher = MockFetcher(rows_to_fetch)
    monkeypatch.setattr(py3odb.cursor.Cursor, "fetchone", fetcher.fetch)
    results = []
    for row in cursor:
        results.append(row[0])
    assert len(results) == 4
    assert results[0] == 1
    assert results[1] == "foo"
    assert results[2] == 3.14159
    assert results[3] is None


def test_bind_parameters(cursor, monkeypatch):
    """Test the inner workings of bind_parameters"""
    def mock_prepare(*args):
        """mock odbql_prepare_v2"""
        pass
    mock_odbql = MockODBQL()
    monkeypatch.setattr(py3odb.cursor.Cursor, "_prepare_statement", mock_prepare)
    monkeypatch.setattr(py3odb.odbql, "odbql_bind_null", mock_odbql.odbql_bind_null)
    monkeypatch.setattr(py3odb.odbql, "odbql_bind_text", mock_odbql.odbql_bind_text)
    monkeypatch.setattr(py3odb.odbql, "odbql_bind_int", mock_odbql.odbql_bind_int)
    monkeypatch.setattr(py3odb.odbql, "odbql_bind_double", mock_odbql.odbql_bind_double)
    cursor.execute(f"CREATE TABLE t_foo AS (a INTEGER, b REAL, c STRING) ON <odb>")
    cursor.execute("INSERT INTO t_foo(x) VALUES(?,?,?)", (1, 2.3, 'foo'))
    assert len(mock_odbql.calls) == 3
    assert mock_odbql.calls[0] == ('int', None, 0, 1)
    assert mock_odbql.calls[1][0] == 'double'
    assert mock_odbql.calls[1][3].value == ctypes.c_double(2.3).value
    assert mock_odbql.calls[2][0] == 'text'
