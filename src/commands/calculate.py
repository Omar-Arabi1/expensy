import click
from colorama import Fore
import sys
import sqlite3

from helpers.get_db_path import get_db_path

@click.command(help='know the amount of money left from your expenses')
@click.argument("balance", type=float)
def calculate(balance: float) -> None:
    """
    calculates the amount of money you have left in your balance
    
    :param balance = your balance, must be greater than the sum of all the things you have in your expenses list
    
    :example >>> expensy calculate <balance>
    """
    if balance <= 0:
        click.echo(Fore.RED + 'Invalid all money, all money must be at least 1$')
        sys.exit()

    select_all_query = """ SELECT * FROM expenses; """

    db_path: str = get_db_path()

    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()

        cursor.execute(select_all_query)

        balance = cursor.fetchall()

        if len(balance) == 0:
            click.echo(Fore.RED + "you have nothing in your expenses, add something with the 'add' command")
            sys.exit()

        prices: list[float] = [expense[1] for expense in balance]

        total_amount_spent: float = sum(prices)

        if total_amount_spent > balance:
            click.echo(Fore.RED + "your balance can't be smaller than all the money spent inside the expenses list")
            sys.exit()

    click.echo(Fore.RED + f"you lost -{total_amount_spent}")

    money_kept: float = round(balance - total_amount_spent, 2)

    click.echo(Fore.GREEN + f"you kept {money_kept}")
