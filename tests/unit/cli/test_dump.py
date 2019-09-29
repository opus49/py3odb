"""Tests for cli/dump module."""
from ...context import py3odb


def test_dump_object(mock_subparsers):
    """Test the dump class."""
    dump_command = py3odb.cli.dump.DumpCommand(mock_subparsers)
    assert isinstance(dump_command, py3odb.cli.dump.DumpCommand)
    assert isinstance(dump_command, py3odb.cli.Command)
