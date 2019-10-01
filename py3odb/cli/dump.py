"""Module for the dump command."""
from collections import OrderedDict
from py3odb import InterfaceError, ProgrammingError, Reader
from py3odb.cli import Command
from py3odb.constants import ColumnType, Varno


class DumpCommand(Command):
    """The dump command."""
    help_text = "Dump information about the ODB2 file (e.g. column names)."

    @property
    def description(self):
        """Describes the dump command."""
        return DumpCommand.help_text

    @staticmethod
    def _get_column_data(filename):
        """Retrieve a dictionary of column names and types."""
        columns = OrderedDict()
        with Reader(filename, "SELECT * FROM <odb>") as odb_reader:
            for column in odb_reader.description:
                columns[column[0]] = ColumnType(column[1]).name
        return columns

    @staticmethod
    def _get_varno_data(filename):
        """Retrieve a sorted list of tuples containing varno code, name, desc."""
        varno_data = []
        with Reader(filename, "SELECT DISTINCT varno@body FROM <odb>") as odb_reader:
            for row in odb_reader:
                code = row["varno@body"]
                name = Varno.get_name(code)
                desc = Varno.get_desc(name) if name != "unknown" else "unknown"
                varno_data.append((code, name, desc))
        if varno_data:
            varno_data.sort(key=lambda x: x[1])
        return varno_data

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

    def command(self, args):
        """Run the dump command."""
        try:
            if args.columns:
                self.print_columns(args.filename, verbose=args.verbose)
            if args.varno:
                self.print_varnos(args.filename, verbose=args.verbose)
        except InterfaceError as err:
            print(f"Dump interface error: {err}")
        except ProgrammingError:
            print(f"Dump error: {args.filename} does not appear to be a valid ODB file.")

    def print_columns(self, filename, verbose=False):
        """Print the columns from an ODB2 file."""
        columns = self._get_column_data(filename)
        if verbose:
            print("-" * 51)
            print(f"{'name':40}type")
            print("-" * 51)
            for column_name in sorted(columns):
                print(f"{column_name:40}{columns[column_name]}")
        else:
            print("-" * 51)
            print("name")
            print("-" * 51)
            for column_name in sorted(columns):
                print(f"{column_name}")

    def print_varnos(self, filename, verbose=False):
        """Print a list of varnos from an ODB2 file."""
        varno_data = self._get_varno_data(filename)
        if varno_data:
            if verbose:
                print("-" * 80)
                print(f"{'name':20}code  description")
                print("-" * 80)
            else:
                print("-" * 25)
                print(f"{'name':20}code")
                print("-" * 25)
            for code, name, desc in varno_data:
                if verbose:
                    print(f"{name:20}{code:-4}  {desc}")
                else:
                    print(f"{name:20}{code:-4}")
        else:
            print(f"No varno's found in {filename}.")
