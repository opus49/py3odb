"""Tests for cli/dump module."""
from argparse import Namespace
import pytest
from ...context import py3odb


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
    assert lines[3].endswith("FLOAT")
    assert lines[4].endswith("FLOAT")
    assert lines[5].endswith("FLOAT")
    assert lines[6].endswith("INTEGER")


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


def test_dump_handles_missing_file(dump_command):
    """Test that the dump command handles non-ODB2 files."""
    try:
        dump_command.command(
            Namespace(filename="doesnotexist.odb", columns=False, varno=True, verbose=False)
        )
    except py3odb.Error:
        pytest.fail("Failed to handle interface error.")


def test_dump_handles_invalid_file(dump_command):
    """Test that the dump command handles non-ODB2 files."""
    try:
        dump_command.command(
            Namespace(filename=f"{__file__}", columns=False, varno=True, verbose=False)
        )
    except py3odb.Error:
        pytest.fail("Failed to handle programming error.")
