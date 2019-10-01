"""Module for the geopoints command."""
import sys
from py3odb import InterfaceError, ProgrammingError, Reader
from py3odb.cli import Command
from py3odb.constants import Varno


class GeopointsCommand(Command):
    """The geopoints command."""
    help_text = "Generate a standard 6-column geopoints file for Metview."""
    desc_text = f"""
{help_text}
You must supply the filename, column, and varno.  You may use the
varno name or code.

Examples:
    $ py3odb geopoints surface.odb -c obsvalue@body -v 39
    $ py3odb geopoints surface.odb -c bgvalue -v t2m

See https://apps.ecmwf.int/odbgov/varno/

"""

    def add_arguments(self):
        super().add_arguments()
        self.parser.add_argument(
            "-c",
            "--column",
            help="The column to include (e.g. obsvalue@body).",
            type=str,
            required=True
        )
        self.parser.add_argument(
            "-v",
            "--varno",
            help="The varno to include.  May be either name or code.",
            required=True
        )

    @property
    def description(self):
        """Describes the geopoints command."""
        return GeopointsCommand.desc_text

    def command(self, args):
        """Run the geopoints command."""
        try:
            gp_manager = GeopointsRunner(args.filename, args.varno, args.column)
            results = gp_manager.run()
            for line in results:
                print(line)
        except InterfaceError as err:
            print(f"Geopoints error: {err}")
        except ProgrammingError:
            print(f"Geopoints error: {args.filename} does not appear to be "
                  "a valid ODB2 file.", file=sys.stderr)


class GeopointsRunner:
    """Class for running geopoints file generation."""
    def __init__(self, filename, varno, column):
        self.filename = filename
        self.varno = self._validate_varno(varno)
        self.column = self._validate_column(column)
        if self.column is None:
            self.error(f"\nCould not find column {column} in {self.filename}.")

    @staticmethod
    def error(message):
        """Handle fatal errors."""
        print(message, file=sys.stderr)
        raise SystemExit(1)

    def generate_header(self):
        """Generate the header for the geopoints file."""
        header = ["#GEO", f"VARNO = {self.varno}", f"COLUMN = {self.column}"]
        header.append("  lat       lon     lvl   date      time      value")
        header.append("#DATA")
        return header

    def generate_sql_command(self):
        """Generate the SQL command from the varno and column."""
        sql_command = f"SELECT lat@hdr,lon@hdr,date@hdr,antime@desc,{self.column} "
        sql_command += f"FROM <odb> WHERE varno={self.varno}"
        return sql_command

    def run(self):
        """Query the database and return a list of lines in geopoints format."""
        results = self.generate_header()
        with Reader(self.filename, self.generate_sql_command()) as odb_reader:
            if len(odb_reader.description) < 5:
                self.error(f"Could not find varno {self.varno} in {self.filename}")
            for row in odb_reader:
                if row[self.column] is None:
                    continue
                line = f"{row['lat@hdr']:8.3f}  {row['lon@hdr']:8.3f}   "
                line += f"0   {row['date@hdr']}   {self._parse_antime(row['antime@desc'])}  "
                line += f"{row[self.column]:12.6f}"
                results.append(line)
        if len(results) < 6:
            self.error(f"Could not find data matching that criteria.")
        return results

    @staticmethod
    def _parse_antime(antime):
        """Convert antime to format geopoints expects."""
        return f"{antime:06}"[:4]

    def _validate_column(self, column):
        """Make sure the column exists and correct if necessary."""
        with Reader(self.filename, "SELECT * FROM <odb> WHERE entryno@body=1") as odb_reader:
            for entry in odb_reader.description:
                if "@" in column:
                    if column == entry[0]:
                        return column
                else:
                    column_tag, _ = entry[0].split("@")
                    if column == column_tag:
                        return entry[0]
        return None

    def _validate_varno(self, raw_varno):
        """Convert the user supplied varno into a usable value."""
        try:
            varno = int(raw_varno)
        except ValueError:
            varno = Varno.get_code(raw_varno)
            if varno == "unknown":
                self.error(f"Unknown varno code: {raw_varno}")
        return varno
