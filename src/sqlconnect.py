import mysql.connector as mysql
db=mysql.connect(
    host='localhost',
    user='root',
    passwd='Jordanstockwolf99',
    database='ipproject')

cursor = db.cursor()
cursor.execute('''use ipproject;''')
cursor.execute('''alter table watchlist modify watchlist varchar(50);''')
db.commit()