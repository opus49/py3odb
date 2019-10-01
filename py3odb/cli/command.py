"""Module for abstract Command class to support argument parsing."""
from abc import ABC, abstractmethod
from argparse import RawTextHelpFormatter


class Command(ABC):
    """Abstract class that defines a command for argument parsing."""
    help_text = None

    def __init__(self, subparsers):
        self.subparsers = subparsers
        self.parser = subparsers.add_parser(
            self.name,
            description=self.description,
            formatter_class=RawTextHelpFormatter
        )
        self.add_arguments()
        self.parser.set_defaults(command=self.command)

    @property
    def name(self):
        """The name of this command."""
        return self.__class__.__name__.replace("Command", "").lower()

    @property
    def description(self):
        """The description to print before help text."""
        return ""

    @abstractmethod
    def add_arguments(self):
        """Add the arguments specific to this command."""
        self.parser.add_argument("filename", help="The ODB2 filename.")

    @abstractmethod
    def command(self, args):
        """The underlying function that is called when a command is selected."""
