import click
import sys
from colorama import Fore
import sqlite3
import datetime
from sqlite3 import IntegrityError

from helpers.get_db_path import get_db_path

@click.command(help='add an expense to your list')
@click.argument('expense')
@click.argument('price', type=float)
def add(expense: str, price: float) -> None:
    """
    adds an expense with a name, price and a an automatic creation date

    creation date is saved in the format of Y-M-D

    :param expense = the expense name must be unique it acts like the id
    :param price = the price of the expense

    :example >>> expensy add <expense> <price>
    """
    if price <= 0:
        click.echo(Fore.RED + 'Invalid price, price must be at least 1$')
        sys.exit()

    current_time: datetime = datetime.datetime.now()
    creation_date: str = str(current_time.date())
    insert_query = "INSERT INTO expenses (expense, price, creation_date) VALUES (?, ?, ?)"
    expense_data = (expense, price, creation_date)

    db_path: str = get_db_path()

    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()

        try:
            cursor.execute(insert_query, expense_data)
        except IntegrityError:
            click.echo(Fore.RED + f"expense entered '{expense}' already exists")
            sys.exit()

        connection.commit()

    click.echo(Fore.GREEN + "added the expense successfully")
