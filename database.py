import sqlite3

def getDBConnection():
    conn = sqlite3.connect('finance_tracker.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = getDBConnection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS income (
                   id INTEGER PRIMARY KEY,
                   amount REAL, 
                   source TEXT, 
                   date TEXT
    )
                   ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expense (
                   id INTEGER PRIMARY KEY,
                   amount REAL, 
                   source TEXT,
                   date TEXT)
                   ''')
    
    
    conn.commit()
    conn.close()

create_tables()

