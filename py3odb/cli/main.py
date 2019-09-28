#!/usr/bin/env python3

"""Main Module for py3odb"""
from argparse import ArgumentParser

from py3odb.cli.command import Command
import py3odb.cli.dump as dump
import py3odb.cli.geopoints as geopoints
import py3odb.cli.query as query


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
    "dump": dump.DumpCommand,
    "geopoints": geopoints.GeopointsCommand,
    "query": query.QueryCommand,
    "help": HelpCommand
}


def usage():
    """Print the usage statement."""
    print("Usage:")
    print("    py3odb <command> [<args>]")
    print("    py3odb help <command>\n")
    print("Available commands:")
    for keyname, class_name in _COMMANDS.items():
        if class_name.help_text is None:
            continue
        print(f"    {keyname:10} {class_name.help_text}")


def main():
    parser = ArgumentParser(add_help=False)
    subparsers = parser.add_subparsers()
    subparsers.required = True
    for command_class in _COMMANDS.values():
        command_class(subparsers)
    try:
        args = parser.parse_args()
        args.command(args)
    except TypeError:
        usage()


if __name__ == "__main__":
    main()
