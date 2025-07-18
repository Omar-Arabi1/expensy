import click
import sqlite3
from colorama import Fore
import sys

@click.command(help='remove an expense from the list')
@click.option('-d', '--remove-date', help='remove all expenses with the same creation date Y-M-D', default='')
@click.argument('expense_name')
def remove(expense_name: str, remove_date: str) -> None:
    if remove_date == '' or len(remove_date.split()) == 0:
        delete_query = """ DELETE FROM expenses WHERE expense = ?; """
        get_expense_name_query = """ SELECT * FROM expenses WHERE expense = ?; """
    else:
        delete_query = """ DELETE FROM expenses WHERE creation_date = ?; """
        get_expesne_date_query = """ SELECT * FROM expenses WHERE creation_date = ?; """

    with sqlite3.connect('expenses.db') as connection:
        cursor = connection.cursor()

        if remove_date == '' or len(remove_date.split()) == 0:
            cursor.execute(get_expense_name_query, (expense_name, ))
            expense = cursor.fetchone()
        else:
            cursor.execute(get_expesne_date_query, (remove_date, ))
            expense = cursor.fetchone()

        if expense is None:
            click.echo(Fore.RED + "the given argument does not exist in the list")
            sys.exit()

        if remove_date != '' or len(remove_date.split()) != 0:
            cursor.execute(delete_query, (remove_date, ))
            click.echo(Fore.GREEN + f"removed all expenses with {remove_date} as their creation_date from list successfully")
        else:
            cursor.execute(delete_query, (expense_name, ))
            click.echo(Fore.GREEN + f"removed '{expense_name}' from list successfully")

        connection.commit()
