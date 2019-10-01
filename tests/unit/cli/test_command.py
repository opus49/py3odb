"""Tests for cli/command module."""
from py3odb.cli import Command


class MockCommand(Command):
    """Mock Command for testing."""
    help_text = "Help for mock command"

    def add_arguments(self):
        """Add arguments to the parser."""
        super().add_arguments()
        self.parser.add_argument(
            "-t",
            "--test",
            help="Test",
            action="store_true"
        )

    def command(self, args):
        """Runs the mock command"""
        pass


def test_command(mock_subparsers):
    """Test the Command abstract class."""
    mock_command = MockCommand(mock_subparsers)
    assert mock_command.name == "mock"
    assert mock_command.description == ""
    assert len(mock_subparsers.parsers) == 1
    parser = mock_subparsers.parsers[0]
    assert parser.args == ('mock',)
    assert parser.arguments[0][0][0] == 'filename'
