"""Used to share fixtures among tests."""
import pytest
from ...context import py3odb
from ...context import main


MOCK_CURSOR_DATA = {
    "SELECT * FROM <odb>": {
        "description": (
            ('lat@hdr', 2, None, None, None, None, None),
            ('lon@hdr', 2, None, None, None, None, None),
            ('varno@body', 1, None, None, None, None, None),
            ('obsvalue@body', 2, None, None, None, None, None)
        ),
        "rows": (
            py3odb.row.Row(
                {"lat@hdr": 23.1, "lon@hdr": 120.3, "varno@body": 1, "obsvalue": 3.2}
            ),
            py3odb.row.Row(
                {"lat@hdr": -13.2, "lon@hdr": -10.3, "varno@body": 2, "obsvalue": 7.8}
            ),
            py3odb.row.Row(
                {"lat@hdr": 3.8, "lon@hdr": 40.2, "varno@body": 3, "obsvalue": -1.2}
            )
        )
    },
    "SELECT DISTINCT varno@body FROM <odb>": {
        "description": (
            ('varno@body', 1, None, None, None, None, None),
        ),
        "rows": (
            py3odb.row.Row({"varno@body": 1}),
            py3odb.row.Row({"varno@body": 2}),
            py3odb.row.Row({"varno@body": 3})
        )
    },
    "empty": {
        "description": (),
        "rows": ()
    }
}


class MockReader:  # pylint: disable=too-few-public-methods
    """Mock Reader object."""
    def __init__(self, sql_command):
        self._iter_index = 0
        self._rows = MOCK_CURSOR_DATA[sql_command]["rows"]
        self._description = MOCK_CURSOR_DATA[sql_command]["description"]

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self._iter_index >= len(self._rows):
            raise StopIteration
        value = self._rows[self._iter_index]
        self._iter_index += 1
        return value

    @property
    def description(self):
        """Return the mock cursor description."""
        return self._description


@pytest.fixture(name="mock_reader_distinct_varno")
def mock_reader_distinct_varno_fixture(monkeypatch):
    """Fixture for mocking a Reader object that acts like a SELECT DISTINCT varno query."""
    def mock_reader(*args):
        """mock reader function"""
        return MockReader("SELECT DISTINCT varno@body FROM <odb>")
    monkeypatch.setattr(py3odb.cli.dump, 'Reader', mock_reader)


@pytest.fixture(name="mock_reader_select_all")
def mock_reader_select_all_fixture(monkeypatch):
    """Fixture for mocking a Reader object that acts like a SELECT * FROM <odb> query."""
    def mock_reader(*args):
        """mock reader function"""
        return MockReader("SELECT * FROM <odb>")
    monkeypatch.setattr(py3odb.cli.dump, 'Reader', mock_reader)
    monkeypatch.setattr(py3odb.cli.query, 'Reader', mock_reader)


@pytest.fixture(name="mock_reader_empty")
def mock_reader_empty_fixture(monkeypatch):
    """Fixture for mocking a Reader object that returns no data."""
    def mock_reader(*args):
        """mock reader function"""
        return MockReader("empty")
    monkeypatch.setattr(py3odb.cli.dump, 'Reader', mock_reader)


@pytest.fixture(name="mock_subparsers")
def mock_subparsers_fixture():
    """Fixture for mocking a subparsers object from argparse."""
    class MockSubparsers:  # pylint: disable=too-few-public-methods
        """Mock subparsers from argparse."""
        def __init__(self):
            self.parsers = []

        def add_parser(self, *args, **kwargs):
            """Add a parser"""
            self.parsers.append(MockParser(*args, **kwargs))
            return self.parsers[-1]

    class MockParser:
        """Mock parser from argparse."""
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.arguments = []
            self.defaults = {}

        def add_argument(self, *args, **kwargs):
            """Add an argument"""
            self.arguments.append((args, kwargs))

        def set_defaults(self, **kwargs):
            """Set a default"""
            for keyname, value in kwargs.items():
                self.defaults[keyname] = value

    return MockSubparsers()


@pytest.fixture(name="usage")
def usage_fixture(capsys):
    """Get the usage output from main."""
    main.usage()
    return capsys.readouterr().out.splitlines()


@pytest.fixture(name="dump_command")
def dump_command_fixture(mock_subparsers):
    """Get a DumpCommand object."""
    return py3odb.cli.dump.DumpCommand(mock_subparsers)


@pytest.fixture(name="query_command")
def query_command_fixture(mock_subparsers):
    """Get a QueryCommand object."""
    return py3odb.cli.query.QueryCommand(mock_subparsers)


@pytest.fixture(name="geopoints_command")
def geopoints_command_fixture(mock_subparsers):
    """Get a GeopointsCommand object."""
    return py3odb.cli.geopoints.GeopointsCommand(mock_subparsers)
