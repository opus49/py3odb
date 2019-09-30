"""Tests for cli/dump module."""
from argparse import Namespace
import pytest
from ...context import py3odb


@pytest.fixture(name="dump_command")
def dump_command_fixture(mock_subparsers):
    """Get a DumpCommand object."""
    return py3odb.cli.dump.DumpCommand(mock_subparsers)


def test_dump_command(dump_command):
    """Generic test the dump class."""
    assert isinstance(dump_command, py3odb.cli.dump.DumpCommand)
    assert isinstance(dump_command, py3odb.cli.Command)


def test_description(dump_command):
    """Test the DumpCommand description property."""
    assert dump_command.description == py3odb.cli.dump.DumpCommand.help_text


def test_prints_columns(mock_reader_select_all, dump_command, capsys):
    """Test the results of the print_columns method."""
    dump_command.command(Namespace(filename="foo", columns=True, varno=False, verbose=False))
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 7
    assert lines[3].startswith("lat@hdr")
    assert lines[4].startswith("lon@hdr")
    assert lines[5].startswith("obsvalue@body")
    assert lines[6].startswith("varno@body")


def test_prints_columns_verbose(mock_reader_select_all, dump_command, capsys):
    """Test the results of the print_columns method with verbosity."""
    dump_command.command(Namespace(filename="foo", columns=True, varno=False, verbose=True))
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 7
    for index in range(3, 7):
        assert lines[index].endswith("INTEGER")


def test_print_varnos(mock_reader_distinct_varno, dump_command, capsys):
    """Test the results of the print_varnos method."""
    dump_command.command(Namespace(filename="foo", columns=False, varno=True, verbose=False))
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 6
    assert lines[3].startswith("t")
    assert lines[3].endswith("2")
    assert lines[4].startswith("u")
    assert lines[4].endswith("3")
    assert lines[5].startswith("z")
    assert lines[5].endswith("1")


def test_print_varnos_verbose(mock_reader_distinct_varno, dump_command, capsys):
    """Test the results of the print_varnos method with verbosity."""
    dump_command.command(Namespace(filename="foo", columns=False, varno=True, verbose=True))
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 6
    assert "upper air temperature" in lines[3]
    assert "upper air u component" in lines[4]
    assert "geopotential" in lines[5]


def test_print_varnos_empty(mock_reader_empty, dump_command, capsys):
    """Test the results of the print_varnos method with no results."""
    dump_command.command(Namespace(filename="foo", columns=False, varno=True, verbose=False))
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 1
