import click
import sqlite3
from colorama import Fore
import sys
import pandas as pd

@click.command(help='export your expenses into csv format')
def export() -> None:
    fetch_all_query = """ SELECT * FROM expenses;"""
    
    with sqlite3.connect('expenses.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute(fetch_all_query)
        
        all_expenses = cursor.fetchall()
        
        if len(all_expenses) == 0:
            click.echo(Fore.RED + "you have nothing in your expenses, add something with the 'add' command")
            sys.exit()
        
        dataframe = pd.read_sql_query(fetch_all_query, connection)
    
    dataframe.to_csv('expenses.csv', index=False)
        
        