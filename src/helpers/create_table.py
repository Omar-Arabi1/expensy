import sqlite3
from helpers.get_db_path import get_db_path

def create_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS expenses (
        expense TEXT UNIQUE PRIMARY KEY,
        price REAL,
        creation_date TEXT
    );
    """
    
    db_path: str = get_db_path()
    
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
    
        cursor.execute(create_table_query)
    
        connection.commit()
