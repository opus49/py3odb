"""Tests for cli/query module."""
from argparse import Namespace
import pytest
from ...context import py3odb


def test_query_command(query_command):
    """Generic test for the query class."""
    assert isinstance(query_command, py3odb.cli.query.QueryCommand)
    assert isinstance(query_command, py3odb.cli.Command)


def test_description(query_command):
    """Test the QueryCommand description property."""
    assert query_command.description == py3odb.cli.query.QueryCommand.desc_text


def test_command(mock_reader_select_all, query_command, capsys):
    """Test the results of the command method."""
    query_command.command(Namespace(filename="foo", sql_command="foo"))
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 3
    assert lines[0] == "(23.1, 120.3, 1, 3.2)"
    assert lines[1] == "(-13.2, -10.3, 2, 7.8)"
    assert lines[2] == "(3.8, 40.2, 3, -1.2)"


def test_query_handles_missing_file(query_command):
    """Test that the query command handles missing files."""
    try:
        query_command.command(
            Namespace(filename="doesnotexist.odb", sql_command="foo")
        )
    except py3odb.Error:
        pytest.fail("Failed to handle interface error.")


def test_query_handles_programming_error(query_command):
    """Test that the query command handles non-ODB2 files or syntax errors."""
    try:
        query_command.command(
            Namespace(filename=f"{__file__}", sql_command="SELECT * FROM <odb>")
        )
        query_command.command(
            Namespace(filename=f"{__file__}", sql_command="I like cheese")
        )
    except py3odb.Error:
        pytest.fail("Failed to handle programming error.")
