"""Integration test for geopoints command."""
from argparse import Namespace
import pytest


def test_geopoints_output_fails_on_bad_column(sample_odb, geopoints_command):
    """Test that the geopoints command fails with an invalid column."""
    with pytest.raises(SystemExit):
        geopoints_command.command(
            Namespace(filename=sample_odb, column="foo", varno="-1", where=None)
        )


def test_geopoints_output_fails_on_bad_varno(sample_odb, geopoints_command):
    """Test that the geopoints command fails with an invalid varno."""
    with pytest.raises(SystemExit):
        geopoints_command.command(
            Namespace(filename=sample_odb, column="obsvalue", varno="-1", where=None)
        )


def test_geopoints_handles_where_syntax_error(sample_odb, geopoints_command):
    """Test that the geopoints command fails with an invalid varno."""
    try:
        geopoints_command.command(
            Namespace(filename=sample_odb, column="obsvalue", varno="162", where="foo >")
        )
    except:  # noqa: E722  # pylint: disable=bare-except
        pytest.fail("Did not handle WHERE syntax error.")
