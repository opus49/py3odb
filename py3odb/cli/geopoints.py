"""Module for the geopoints command."""
from collections import defaultdict as ddict
from datetime import datetime as dt
from warnings import warn
from py3odb import Reader
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
    $ py3odb geopoints surface.odb -c bgvalue@body -v t2m

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
        pass
