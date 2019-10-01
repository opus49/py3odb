"""Tests for cli/query module."""
from ...context import py3odb


def test_geopoints_command(geopoints_command):
    """Generic test for the gepoints class."""
    assert isinstance(geopoints_command, py3odb.cli.geopoints.GeopointsCommand)
    assert isinstance(geopoints_command, py3odb.cli.Command)


def test_description(geopoints_command):
    """Test the GeopointsCommand description property."""
    assert geopoints_command.description == py3odb.cli.geopoints.GeopointsCommand.desc_text
