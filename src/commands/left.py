import click
from colorama import Fore
import sys
import sqlite3

@click.command(help='know the amount of money left from your expenses')
@click.argument("all_money")
def left(all_money: str) -> None:
    try:
        all_money: float = float(all_money)
    except ValueError:
        all_money_type = type(all_money).__name__
        click.echo(Fore.RED + f"expected price to be a float got {all_money_type}")
        sys.exit()

    if all_money <= 0:
        click.echo(Fore.RED + 'Invalid all money, all money must be at least 1$')
        sys.exit()

    select_all_query = """ SELECT * FROM expenses;"""

    with sqlite3.connect('expenses.db') as connection:
        cursor = connection.cursor()

        cursor.execute(select_all_query)

        all_expenses = cursor.fetchall()

        if len(all_expenses) == 0:
            click.echo(Fore.RED + "you have nothing in your expenses, add something with the 'add' command")
            sys.exit()

        prices: list[float] = [expense[1] for expense in all_expenses]

        total_amount_spent: float = sum(prices)

        if total_amount_spent > all_money:
            click.echo(Fore.RED + "all the money you spent can not be smaller than all the money inside the expenses list")
            sys.exit()

    click.echo(Fore.RED + f"you lost -{total_amount_spent}")

    money_kept: float = round(all_money - total_amount_spent, 2)

    click.echo(Fore.GREEN + f"you kept {money_kept}")
