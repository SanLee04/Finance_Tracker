from database import getDBConnection

class Income:
    def __init__(self, amount, source, date):
        self.amount = amount 
        self.source = source
        self.date = date


    def save(self): 
        conn = getDBConnection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO income(amount, source, date) VALUES(?, ?, ?)
                       ''', (self.amount, self.source, self.date))
        conn.commit()
        conn.close()

        



class Expense: 
    def __init__(self, amount, source, date):
        self.amount = amount 
        self.source = source
        self.date = date

    
    def save(self): 
        conn = getDBConnection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO income(amount, source, date) VALUES(?, ?, ?)
                       ''', (self.amount, self.source, self.date))
        conn.commit()
        conn.close()


def get_all_incomes():
    conn = getDBConnection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM income')
    incomes = cursor.fetchall()
    conn.close()
    return incomes


def get_all_expenses(): 
    conn = getDBConnection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM income')
    expenses = cursor.fetchall()
    conn.close()
    return expenses


