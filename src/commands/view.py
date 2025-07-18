import click
import pandas as pd
import sqlite3
from colorama import Fore, Style
import sys

from helpers.get_db_path import get_db_path

@click.command(help='view all your expenses')
def view() -> None:
    db_path: str = get_db_path()
    
    with sqlite3.connect(db_path) as connection:        
        select_all_query = """ SELECT * FROM expenses; """
        
        dataframe = pd.read_sql_query(select_all_query, connection)
        
        if dataframe.empty is True:
            click.echo(Fore.RED + "you have nothing in your expenses, add something with the 'add' command")
            sys.exit()
    
    click.echo(Fore.BLUE + Style.BRIGHT + "expenses:" + Fore.RESET + Style.RESET_ALL)
    click.echo(dataframe)