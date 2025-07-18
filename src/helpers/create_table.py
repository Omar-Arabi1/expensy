import sqlite3

def create_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS expenses (
        expense TEXT UNIQUE PRIMARY KEY,
        price REAL,
        creation_date TEXT
    );
    """
    
    with sqlite3.connect('expenses.db') as connection:
        cursor = connection.cursor()
    
        cursor.execute(create_table_query)
    
        connection.commit()
