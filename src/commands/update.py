import click
import sqlite3
from colorama import Fore
import sys

from helpers.get_db_path import get_db_path

@click.command(help="update an expense's price")
@click.argument('expense_name')
@click.argument('new_price', type=float)
def update(expense_name: str, new_price: float) -> None:
    """
    updates an existing expense's price
    
    :param expense_name = the expense name to update its price
    :param new_price = the price to update the expense with
    
    :example >>> expensy update <expense_name> <new_price>
    """
    update_query = """ UPDATE expenses SET price = ? WHERE expense = ?; """
    get_expense_name_query = """ SELECT * FROM expenses WHERE expense = ?; """

    db_path: str = get_db_path()

    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()

        cursor.execute(get_expense_name_query, (expense_name, ))
        expense = cursor.fetchone()

        if expense is None:
            click.echo(Fore.RED + f"'{expense_name}' does not exist in your list")
            sys.exit()

        cursor.execute(update_query, (new_price, expense_name, ))

        connection.commit()

    click.echo(Fore.GREEN + f"updated '{expense_name}' successfully")