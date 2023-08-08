import mysql.connector as mysql
import pandas as pd
db=mysql.connect(host="localhost",user="root",passwd="Guru@56755",database = "project")
cur = db.cursor()
lis=[]
cur.execute("select * from corporate;")
record = cur.fetchall()
for x in record:
    lis.append(x)
df=pd.DataFrame(lis,columns=['company','symbol'])
print(df['company'])


