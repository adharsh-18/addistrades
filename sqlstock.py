import mysql.connector as mysql
from datetime import date 

db=mysql.connect(
    host='localhost',
    user='root',
    password='Jordanstockwolf99',
    database='ipproject')

def add_stock(a,b,c,d):
    cursor1 = db.cursor()
    cursor1.execute('''use ipproject;''')
    cursor1.execute('''insert into stock values(%s,%s,%s,%s,%s,'buy');''',(a,b,c,d,date.today(),))
    db.commit()
    
def add_watchlist(a,b):
    cursor2 = db.cursor()
    cursor2.execute('''use ipproject;''')
    cursor2.execute('''insert into watchlist values(%s,%s);''',(a,b,))
    db.commit()
    
def remove_watchlist(a,b):
    cursor2 = db.cursor()
    cursor2.execute('''use ipproject;''')
    cursor2.execute('''delete from watchlist where username = %s and watchlist = %s;''',(a,b,))
    db.commit()
    
def get_watchlist(a):
    cursor3 = db.cursor()
    cursor3.execute('''use ipproject;''')
    cursor3.execute('''select watchlist from watchlist where username =%s''',(a,))
    record = cursor3.fetchall()
    db.commit()
    return record

def my_stocks(a):
    cursor4 = db.cursor()
    cursor4.execute('''use ipproject;''')
    cursor4.execute('''select distinct(company) from stock where username = %s;''',(a,))
    record = cursor4.fetchall()
    db.commit()
    return record

def my_stocks_quantity(a,b):
    cursor4 = db.cursor()
    cursor4.execute('''use ipproject;''')
    cursor4.execute('''select sum(quantity) from stock where username = %s and company = %s group by company,operation ;''',(a,b,))
    record = cursor4.fetchall()
    db.commit()
    return record


def my_history(a):
    cursor4 = db.cursor()
    cursor4.execute('''use ipproject;''')
    cursor4.execute('''select date , company,quantity,buy_rate,operation from stock where username = %s;''',(a,))
    record = cursor4.fetchall()
    db.commit()
    return record

def remove_stock(a,b,c,d):
    cursor4 = db.cursor()
    cursor4.execute('''use ipproject;''')
    cursor4.execute('''insert into stock values(%s,%s,%s,%s,%s,'sell');''',(a,b,c,d,date.today(),))
    db.commit()
    
def sell_value(a):
    cursor4 = db.cursor()
    cursor4.execute('''use ipproject;''')
    cursor4.execute(''' select company,sum(quantity*buy_rate) as cost from stock where username=%s and operation='sell' group by company;;''',(a,))
    return cursor4.fetchall()

def become_pro(a):
    cursor5 = db.cursor()
    cursor5.execute('''use ipproject;''')
    cursor5.execute('''update customer set membership = 'pro' where username = %s;''',(a,))
    db.commit()
    
    
def add_money(a,b):
    cursor6 = db.cursor()
    cursor6.execute('''use ipproject;''')
    cursor6.execute('''update customer set cash = (cash + %s) where username = %s;''',(b,a,))
    db.commit()
def show_balance(a):
    cursor6 = db.cursor()
    cursor6.execute('''use ipproject;''')
    cursor6.execute('''select cash from customer where username = %s;''',(a,))
    return cursor6.fetchall()[0][0]

def take_money(a,b):
    cursor6 = db.cursor()
    cursor6.execute('''use ipproject;''')
    cursor6.execute('''update customer set cash = (cash - %s) where username = %s;''',(b,a,))
    db.commit()
    
    
def change_pass(a,b):
    cursor6 = db.cursor()
    cursor6.execute('''use ipproject;''')
    cursor6.execute('''update customer set password = %s where username = %s;''',(b,a,))
    db.commit()
    
def total_spend(a):
    cursor6 = db.cursor()
    cursor6.execute('''use ipproject;''')
    cursor6.execute('''select company,sum(quantity*buy_rate) as cost from stock where username = %s and operation = 'buy' group by company;''',(a,))
    return cursor6.fetchall()
