"""Module for the query command."""
from py3odb import InterfaceError, ProgrammingError, Reader
from py3odb.cli import Command


class QueryCommand(Command):
    """The query command."""
    help_text = "Execute an SQL-like query against an ODB2 file."
    desc_text = f"""
{help_text}
You can replace the filename reference in the SQL command with <odb>.

Examples:
    $ py3odb query foo.odb "SELECT DISTINCT varno FROM 'foo.odb'"
    $ py3odb query foo.odb "SELECT lat,lon,obsvalue FROM <odb>"

"""

    def add_arguments(self):
        """Add the arguments specific to this command."""
        super().add_arguments()
        self.parser.add_argument(
            "sql_command",
            help="The SQL commmand to execute.  Use <odb> to reference the filename.",
            type=str
        )

    @property
    def description(self):
        """Describes the query command."""
        return QueryCommand.desc_text

    def command(self, args):
        """Run the query command."""
        try:
            with Reader(args.filename, args.sql_command) as odb_reader:
                for row in odb_reader:
                    print(row)
        except InterfaceError as err:
            print(f"Query interface error: {err}")
        except ProgrammingError as err:
            if "Assertion failed" in str(err):
                print(f"Query error: {args.filename} does not appear to be a valid ODB2 file.")
            else:
                print(f"Query error: {err}")
