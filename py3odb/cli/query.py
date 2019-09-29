"""Module for the query command."""
from py3odb import connect
from py3odb.cli import Command


class QueryCommand(Command):
    """The query command."""
    help_text = "Execute an SQL-like query against an ODB2 file."
    desc = f"""
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
        return QueryCommand.desc

    def command(self, args):
        """Run the query command."""
        main(args)


def parse_sql_command(sql_command, filename):
    """Replace <odb> with filename if applicable."""
    if "<odb>" in sql_command:
        sql_command = sql_command.replace("<odb>", f"'{filename}'")
    return sql_command


def main(args):
    """The main function for this script."""
    conn = connect(args.filename)
    cur = conn.cursor()
    cur.execute(parse_sql_command(args.sql_command, args.filename))
    for row in cur:
        print(row)
    conn.close()
