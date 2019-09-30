"""Test the Command Line Interface (CLI)."""
import pytest
import sys
from ..context import py3odb
from ..context import main


@pytest.fixture(name="usage")
def usage_fixture(capsys):
    """Get the usage output from main."""
    main.usage()
    return capsys.readouterr().out.splitlines()


def test_cli_usage(monkeypatch, usage, capsys):
    """Test the usage function."""
    monkeypatch.setattr(sys, "argv", ["foo"])
    main.main()
    result_lines = capsys.readouterr().out.splitlines()
    assert len(result_lines) == len(usage)


def test_cli_version(monkeypatch, capsys):
    """Test printing the version."""
    monkeypatch.setattr(sys, "argv", ["foo", "--version"])
    main.main()
    result_lines = capsys.readouterr().out.splitlines()
    assert result_lines[0] == f"py3odb version {py3odb.__version__}"


def test_cli_help(monkeypatch, usage, capsys):
    """Test the help command without argument."""
    monkeypatch.setattr(sys, "argv", ["foo", "help"])
    main.main()
    result_lines = capsys.readouterr().out.splitlines()
    assert len(result_lines) == len(usage)
