"""Module for the query command."""
from py3odb.cli.command import Command


class QueryCommand(Command):
    """The query command."""
    help_text = "Execute an SQL-like query against an ODB2 file."

    def add_arguments(self):
        """Add the arguments specific to this command."""
        super().add_arguments()
        self.parser.add_argument(
            "sql_command",
            help="The SQL commmand to execute.",
            type=str
        )

    @property
    def description(self):
        """Describes the query command."""
        return QueryCommand.help_text

    def command(self, args):
        """Run the query command."""
        main(args)


def main(args):
    """The main function for this script."""
    print("Running a query...")
