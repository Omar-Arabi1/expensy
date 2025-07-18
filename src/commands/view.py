import click
import pandas as pd
import sqlite3
from colorama import Fore, Style
import sys

@click.command(help='view all your expenses')
def view() -> None:
    with sqlite3.connect('expenses.db') as connection:        
        select_all_query = """ SELECT * FROM expenses; """
        
        dataframe = pd.read_sql_query(select_all_query, connection)
        
        if dataframe.empty is True:
            click.echo(Fore.RED + "you have nothing in your expenses, add something with the 'add' command")
            sys.exit()
    
    click.echo(Fore.BLUE + Style.BRIGHT + "expenses:" + Fore.RESET + Style.RESET_ALL)
    click.echo(dataframe)