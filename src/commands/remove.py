import click
import sqlite3
from colorama import Fore
import sys

@click.command(help='remove an expense from the list')
@click.argument('expense_name')
def remove(expense_name: str) -> None:
    delete_query = """ DELETE FROM expenses WHERE expense = ?; """
    get_expense_name_query = """ SELECT * FROM expenses WHERE expense = ? """

    with sqlite3.connect('expenses.db') as connection:
        cursor = connection.cursor()

        cursor.execute(get_expense_name_query, (expense_name, ))
        expense = cursor.fetchone()

        if expense is None:
            click.echo(Fore.RED + f"'{expense_name}' does not exist in your list")
            sys.exit()

        cursor.execute(delete_query, (expense_name,))

        connection.commit()

    click.echo(Fore.GREEN + f"removed '{expense_name}' from list successfully")
