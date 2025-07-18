import click
import sys
from colorama import Fore
import sqlite3
from uuid import uuid4
import datetime

@click.command(help='add an expense to your list')
@click.argument('expense')
@click.argument('price')
def add(expense: str, price: str) -> None:
    try:
        price: float = float(price)
    except ValueError:
        price_type = type(price).__name__
        click.echo(Fore.RED + f"expected price to be a float got {price_type}")
        sys.exit()

    if price <= 0:
        click.echo(Fore.RED + 'Invalid price, price must be at least 1$')
        sys.exit()
    
    current_time: datetime = datetime.datetime.now()
    creation_date: str = str(current_time.date())
    insert_query = "INSERT INTO expenses (id, expense, price, creation_date) VALUES (?, ?, ?, ?)"
    expense_data = (str(uuid4()), expense, price, creation_date)

    with sqlite3.connect('expenses.db') as connection:
        cursor = connection.cursor()

        cursor.execute(insert_query, expense_data)

        connection.commit()
    
    click.echo(Fore.GREEN + "added the expense successfully")