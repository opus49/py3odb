"""Test the Command Line Interface (CLI)."""
import sys
from ...context import py3odb
from ...context import main


def test_main_usage(monkeypatch, usage, capsys):
    """Test the usage function."""
    monkeypatch.setattr(sys, "argv", ["foo"])
    main.main()
    result_lines = capsys.readouterr().out.splitlines()
    assert len(result_lines) == len(usage)


def test_main_version(monkeypatch, capsys):
    """Test printing the version."""
    monkeypatch.setattr(sys, "argv", ["foo", "--version"])
    main.main()
    result_lines = capsys.readouterr().out.splitlines()
    assert result_lines[0] == f"py3odb version {py3odb.__version__}"


def test_main_help(monkeypatch, usage, capsys):
    """Test the help command without argument."""
    monkeypatch.setattr(sys, "argv", ["foo", "help"])
    main.main()
    result_lines = capsys.readouterr().out.splitlines()
    assert len(result_lines) == len(usage)


def test_main_help_query(monkeypatch, capsys):
    """Test the help command with the query argument."""
    monkeypatch.setattr(sys, "argv", ["foo", "help", "query"])
    main.main()
    result_lines = capsys.readouterr().out.splitlines()
    assert result_lines[0] == "usage: foo query [-h] filename sql_command"
