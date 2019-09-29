#!/usr/bin/env python3

"""Main Module for py3odb command-line interface."""
from argparse import ArgumentParser

from py3odb import __version__
from py3odb.cli import Command, DumpCommand, GeopointsCommand, QueryCommand


class HelpCommand(Command):
    """The dump command."""
    def add_arguments(self):
        self.parser.add_argument("name", nargs="?", help="The command")

    def command(self, args):
        """Run the help command."""
        if args.name and args.name in self.subparsers.choices:
            self.subparsers.choices[args.name].print_help()
        else:
            usage()


_COMMANDS = {
    "dump": DumpCommand,
    "geopoints": GeopointsCommand,
    "query": QueryCommand,
    "help": HelpCommand
}


def usage():
    """Print the usage statement."""
    print("Usage:")
    print("    py3odb <command> [<args>]")
    print("    py3odb help <command>")
    print("    py3odb --version\n")
    print("Available commands:")
    for keyname, class_name in _COMMANDS.items():
        if class_name.help_text is None:
            continue
        print(f"    {keyname:10} {class_name.help_text}")


def main():
    """Main function"""
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
    )
    subparsers = parser.add_subparsers(dest="command")
    for command_class in _COMMANDS.values():
        command_class(subparsers)
    args = parser.parse_args()
    if args.version:
        print(f"py3odb version {__version__}")
    elif args.command is not None:
        try:
            args.command(args)
        except KeyboardInterrupt:
            print("\n")
            raise SystemExit(1)
    else:
        usage()


if __name__ == "__main__":
    main()
