import sqlite3

def getDBConnection():
    conn = sqlite3.connect('finance_tracker.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = getDBConnection
    cursor = conn.cursor()
    

