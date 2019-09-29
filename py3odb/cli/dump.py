"""Module for the dump command."""
from py3odb import connect
from py3odb.cli import Command
from py3odb.constants import ColumnType, Varno


class DumpCommand(Command):
    """The dump command."""
    help_text = "Dump information about the ODB2 file (e.g. column names)."

    def add_arguments(self):
        super().add_arguments()
        self.parser.add_argument(
            "-c",
            "--columns",
            help="Print the columns.",
            action="store_true"
        )
        self.parser.add_argument(
            "-v",
            "--varno",
            help="Print the varnos.",
            action="store_true"
        )
        self.parser.add_argument(
            "-vv",
            "--verbose",
            help="Print full details.",
            action="store_true"
        )

    @property
    def description(self):
        """Describes the dump command."""
        return DumpCommand.help_text

    def command(self, args):
        """Run the dump command."""
        main(args)


def print_columns(filename, verbose=False):
    """Print the columns from an ODB2 file."""
    conn = connect(filename)
    cur = conn.cursor()
    cur.execute("SELECT * FROM <odb>")
    columns = {}
    for column in cur.description:
        columns[column[0]] = ColumnType(column[1]).name
    if verbose:
        print(f"{'name':40}type")
        print("-" * 51)
        for column_name in sorted(columns):
            print(f"{column_name:40}{columns[column_name]}")
    else:
        print("name")
        print("-" * 51)
        for column_name in sorted(columns):
            print(f"{column_name}")
    conn.close()


def _get_varno_data(filename):
    """Retrieve a sorted list of tuples containing varno, code, desc."""
    varno_data = []
    conn = connect(filename)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT varno@body FROM <odb>")
    for row in cur:
        varno = row["varno@body"]
        code = Varno.get_code(varno)
        desc = Varno.get_desc(code) if code != "unknown" else "unknown"
        varno_data.append((varno, code, desc))
    conn.close()
    if varno_data:
        varno_data.sort(key=lambda x: x[1])
    return varno_data


def print_varnos(filename, verbose=False):
    """Print a list of varnos from an ODB2 file."""
    varno_data = _get_varno_data(filename)
    if verbose:
        print(f"{'code':19}varno description")
        print("-" * 80)
    else:
        print(f"{'code':20}varno")
        print("-" * 25)
    for varno, code, desc in varno_data:
        if verbose:
            print(f"{code:20}{varno:-4} {desc:55}")
        else:
            print(f"{code:20}{varno:-4}")


def main(args):
    """Main function."""
    if args.columns:
        print_columns(args.filename, verbose=args.verbose)
    if args.varno:
        print_varnos(args.filename, verbose=args.verbose)
