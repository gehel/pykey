#!/usr/bin/env python
"""Program entry point"""

from __future__ import print_function

import argparse
import sys

import metadata
from mappings.basic import key_combinations, mod_mapping
from PyKey import PyKey, print_devices


def main(argv):
    """Program entry point.

    :param argv: command-line arguments
    :type argv: :class:`list`
    """
    author_strings = []
    for name, email in zip(metadata.authors, metadata.emails):
        author_strings.append('Author: {0} <{1}>'.format(name, email))

    epilog = '''
{project} {version}

{authors}
URL: <{url}>
'''.format(
        project=metadata.project,
        version=metadata.version,
        authors='\n'.join(author_strings),
        url=metadata.url)

    arg_parser = argparse.ArgumentParser(
        prog=argv[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=metadata.description,
        epilog=epilog)
    arg_parser.add_argument(
        '-V', '--version',
        action='version',
        version='{0} {1}'.format(metadata.project, metadata.version))
    arg_parser.add_argument(
        '-d', '--device',
        help='device to bind to, for example /dev/input/event1')
    arg_parser.add_argument(
        '-l', '--list-devices',
        action='store_true',
        help='print description of all input devices')
    arg_parser.add_argument(
        '-p', '--print-keys',
        action='store_true',
        help='print every key press, useful for debugging')

    args = arg_parser.parse_args(args=argv[1:])

    if not (args.list_devices or args.device):
        arg_parser.error('No action requested, add --list-devices or --device')

    print(epilog)

    if args.list_devices:
        print_devices()
    elif args.device:
        py_key = PyKey(
            device_name=args.device,
            mod_mapping=mod_mapping,
            key_mapping=key_combinations,
            print_keys=args.print_keys)

        try:
            py_key.start()
        except KeyboardInterrupt:
            py_key.close()

    return 0


def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    raise SystemExit(main(sys.argv))

if __name__ == '__main__':
    entry_point()
