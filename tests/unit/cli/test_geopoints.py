"""Tests for cli/query module."""
from argparse import Namespace
import pytest
from ...context import py3odb


def test_geopoints_command(geopoints_command):
    """Generic test for the gepoints class."""
    assert isinstance(geopoints_command, py3odb.cli.geopoints.GeopointsCommand)
    assert isinstance(geopoints_command, py3odb.cli.Command)


def test_description(geopoints_command):
    """Test the GeopointsCommand description property."""
    assert geopoints_command.description == py3odb.cli.geopoints.GeopointsCommand.desc_text


def test_geopoints_handles_missing_file(geopoints_command):
    """Test that the geopoints command handles non-ODB2 files."""
    try:
        geopoints_command.command(
            Namespace(filename="doesnotexist.odb", column="foo", varno=-1)
        )
    except py3odb.Error:
        pytest.fail("Failed to handle interface error.")


def test_geopoints_handles_invalid_file(geopoints_command):
    """Test that the geopoints command handles non-ODB2 files."""
    try:
        geopoints_command.command(
            Namespace(filename=f"{__file__}", column="foo", varno=-1)
        )
    except py3odb.Error:
        pytest.fail("Failed to handle programming error.")
