"""Integration test for geopoints command."""
from argparse import Namespace
import sys
from subprocess import run, PIPE
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
    except:  # noqa: E722
        pytest.fail("Did not handle WHERE syntax error.")


def test_geopoints_output(main_program, sample_odb, geopoints_command):
    """Test that the geopoints command works correctly."""
    proc_args = [
        sys.executable,
        main_program,
        "geopoints",
        sample_odb,
        "-c",
        "obsvalue",
        "-v",
        "162"
    ]
    proc = run(proc_args, stdin=PIPE, stdout=PIPE)
    output = proc.stdout.decode().splitlines()
    assert len(output) == 229
    assert output[0].startswith("#GEO")
    assert output[4].startswith("#DATA")
    assert output[5].endswith("0.013709")


def test_geopoints_output_with_where(main_program, sample_odb, geopoints_command):
    """Test that the geopoints command works correctly with constraints."""
    proc_args = [
        sys.executable,
        main_program,
        "geopoints",
        sample_odb,
        "-c",
        "obsvalue",
        "-v",
        "162",
        "--where",
        "vertco_reference_1 > 6457400"
    ]
    proc = run(proc_args, stdin=PIPE, stdout=PIPE)
    output = proc.stdout.decode().splitlines()
    assert len(output) == 7
    assert output[5].endswith("0.000001")
    assert output[6].endswith("0.000002")
