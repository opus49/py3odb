"""Module for the geopoints command."""
from py3odb.cli.command import Command


class GeopointsCommand(Command):
    """The geopoints command."""
    help_text = "Generate a geopoints compatible output given a list of varnos."""

    def add_arguments(self):
        super().add_arguments()
        self.parser.add_argument(
            "-c",
            "--codes",
            help="A comma-separated list of variable codes.",
            type=str
        )

        self.parser.add_argument(
            "-v",
            "--varnos",
            help="A comma-separated list of variable numbers (varno).",
            type=str
        )

    @property
    def description(self):
        """Describes the geopoints command."""
        return GeopointsCommand.help_text

    def command(self, args):
        """Run the geopoints command."""
        main(args)


def main(args):
    """The main function."""
    print("Running the geopoints command...")
