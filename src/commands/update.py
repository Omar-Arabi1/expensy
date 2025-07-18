import click
import sqlite3
from colorama import Fore
import sys

@click.command(help="update an expense's price or name")
@click.argument('expense_name')
@click.argument('new_price')
def update(expense_name: str, new_price: str) -> None:
    update_query = """ UPDATE expenses SET price = ? WHERE expense = ?; """
    get_expense_name_query = """ SELECT * FROM expenses WHERE expense = ?; """

    with sqlite3.connect('expenses.db') as connection:
        cursor = connection.cursor()

        cursor.execute(get_expense_name_query, (expense_name, ))
        expense = cursor.fetchone()

        if expense is None:
            click.echo(Fore.RED + f"'{expense_name}' does not exist in your list")
            sys.exit()

        cursor.execute(update_query, (new_price, expense_name, ))

        connection.commit()

    click.echo(Fore.GREEN + f"updated '{expense_name}' successfully")