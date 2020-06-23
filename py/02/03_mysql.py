import pymysql
#pip install PyMySQL

db = pymysql.connect(
    host="localhost",
    port=3306,
    user='eprot',
    passwd='1234',
    db='mydb'
)

cursor=db.cursor()

cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("database version : %s"%data)

import mysql.connector
#pip install mysql.connector
#pip list | grep 'mysql'

