"""Tests for cli/query module."""
from argparse import Namespace
import pytest
from ...context import py3odb


@pytest.fixture(name="query_command")
def query_command_fixture(mock_subparsers):
    """Get a QueryCommand object."""
    return py3odb.cli.query.QueryCommand(mock_subparsers)


def test_query_command(query_command):
    """Generic test for the query class."""
    assert isinstance(query_command, py3odb.cli.query.QueryCommand)
    assert isinstance(query_command, py3odb.cli.Command)


def test_description(query_command):
    """Test the QueryCommand description property."""
    assert query_command.description == py3odb.cli.query.QueryCommand.desc_text
