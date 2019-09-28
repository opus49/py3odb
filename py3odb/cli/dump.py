"""Module for the dump command."""
from py3odb.cli.command import Command


class DumpCommand(Command):
    """The dump command."""
    help_text = "Dump information about the ODB2 file (e.g. column names)."

    def add_arguments(self):
        super().add_arguments()
        self.parser.add_argument("-c", "--c", help="Print the columns.", action="store_true")
        self.parser.add_argument("-v", "--v", help="Print the varnos.", action="store_true")

    @property
    def description(self):
        """Describes the dump command."""
        return DumpCommand.help_text

    def command(self, args):
        """Run the dump command."""
        main(args)


def main(args):
    """Main function."""
    print("Running the dump command...")
