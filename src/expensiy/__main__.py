#!/usr/bin/env python3

import click

from . import __version__
from commands import add, remove, view, update, calculate, export

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
prog_name: str = 'expensiy'
@click.group(context_settings=CONTEXT_SETTINGS, help="an expense tracker to make it easy to manage expenses")
@click.version_option(__version__, '-v', '--version', prog_name=prog_name, message=f'{prog_name} v{__version__}')
def main() -> None:
    pass

main.add_command(add.add)
main.add_command(remove.remove)
main.add_command(view.view)
main.add_command(update.update)
main.add_command(calculate.calculate)
main.add_command(export.export)

if __name__ == '__main__':
    main()