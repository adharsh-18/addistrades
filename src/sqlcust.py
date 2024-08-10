import mysql.connector as mysql
db=mysql.connect(
    host='localhost',
    user='root',
    password='Jordanstockwolf99',
    database='ipproject')
def add_data(a,b,c,d,e,f):
    h = 'no pro'
    cursor1 = db.cursor()
    cursor1.execute('''use ipproject;''')
    cursor1.execute('''insert into customer values(%s,%s,%s,%s,%s,%s,%s,0);''',(a,b,c,d,e,f,h,))
    db.commit()
    
def get_data(a):
    
    cursor2 = db.cursor()
    cursor2.execute('''use ipproject;''')
    cursor2.execute('''select * from customer where username = %s;''',(a,))
    record = cursor2.fetchall()
    db.commit()
    return record

def all_data():
    
    cursor3 = db.cursor()
    cursor3.execute('''use ipproject;''')
    cursor3.execute('''select * from customer;''')
    record = cursor3.fetchall()
    db.commit()
    return record

def history():
    cursor3 = db.cursor()
    cursor3.execute('''use ipproject;''')
    cursor3.execute('''select * from stock;''')
    record = cursor3.fetchall()
    db.commit()
    return record




