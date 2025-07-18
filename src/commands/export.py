import click
import sqlite3
from colorama import Fore
import sys
import pandas as pd
import os

from helpers.output_file_exceptions_handler import output_file_exception_handler, NoDesiredExtention, FileAlreadyExists, FileDirectoryDoesNotExist
from helpers.get_db_path import get_db_path

@click.command(help='export your expenses into csv format')
@click.option('-o', '--output', help='select the place and name of the output file', default='')
def export(output: str) -> None:
    fetch_all_query = """ SELECT * FROM expenses;"""

    db_path: str = get_db_path()

    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()

        cursor.execute(fetch_all_query)

        all_expenses = cursor.fetchall()

        if len(all_expenses) == 0:
            click.echo(Fore.RED + "you have nothing in your expenses, add something with the 'add' command")
            sys.exit()

        dataframe = pd.read_sql_query(fetch_all_query, connection)

    if output != '' or len(output.split()) != 0:
        try:
            output_file_exception_handler(output_file=output)
            dataframe.to_csv(output, index=False)
            click.echo(Fore.GREEN + f"conversion done successfully at {output}")
        except (NoDesiredExtention, FileAlreadyExists, FileDirectoryDoesNotExist) as err:
            click.echo(err)
            sys.exit()

    current_working_directory: str = os.getcwd()
    expenses_csv_path: str = os.path.join(current_working_directory, 'expenses.csv')

    if os.path.exists(expenses_csv_path) is True:
        click.echo(Fore.RED + f"the default output location {expenses_csv_path} already exists and can't be overwritten use '--output' option or delete the file to continue")
        sys.exit()

    dataframe.to_csv('expenses.csv', index=False)

    click.echo(Fore.GREEN + f"conversion done successfully at {expenses_csv_path}")
