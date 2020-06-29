import mysql.connector
#pip install mysql.connector
#pip list | grep 'mysql'

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

#creating table
sql = "CREATE TABLE customers(" \
      "name VARCHAR(255)," \
      "address VARCHAR(255))"
cursor.execute(sql)

#check if table exists
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)

# add primary key
sql = "ALTER TABLE customers " \
      "ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
cursor.execute(sql)

#insert data into table
sql = "INSERT INTO customers(name, address) "
sql+= "VALUES(%s, %s)"
val=("John", "Highway 21")
cursor.execute(sql, val)
db.commit()

#insert 2
sql="INSERT INTO customers(name, address) VALUES(%s, %s)"
val=[
    ("Peter", "LowStreet 4"),
    ("Amy", "Apple st 652"),
    ("Hannah", "Mountain 21"),
    ("Michael", "Valley 345"),
    ("Sandy", "Ocean blvd 2"),
    ("Betty", "Green Grass 1"),
    ("Richard", "Sky st 331"),
    ("Susan", "One way 98"),
    ("Vicky", "Yellow Garden 2"),
    ("Ben", "Park Lane 38"),
    ("William", "Central st 954"),
    ("Chuck", "Main Road 989"),
    ("Viola", "Sideway 1633")
]

cursor.executemany(sql, val)
db.commit()
print(cursor.rowcount, "was inserted...")

#Get Inserted ID
sql = "INSERT INTO customers(name, address) VALUES(%s, %s)"
val = ("Michelle", "Blue Village")
cursor.execute(sql, val)
db.commit()
print("1 record inserted, ID:",cursor.lastrowid)

#Select from table
var = cursor.execute("SELECT * FROM customers")
print(var)
myresult = cursor.fetchall()
type(myresult)
for x in myresult:
    print(x)

#using the fetchone() method
#fetchone() method will return the first row of the result
cursor.execute("SELECT * FROM customers")
myresult=cursor.fetchone()
print(myresult)

#select with a filter
sql="SELECT * FROM customers WHERE address LIKE '%a%'"
cursor.execute(sql)
myresult=cursor.fetchall()
for x in myresult:
    print(x)

#Wildcard Characters
sql="SELECT * FROM customers WHERE address LIKE '%way%'"
cursor.execute(sql)
myresult=cursor.fetchall()
for x in myresult:
    print(x)

#Prevent SQL injection
sql="SELECT * FROM customers WHERE address = %s"
adr=("Yellow Garden 2") #comma
cursor.execute(sql, adr)
myresult = cursor.fetchall()
for x in myresult:
    print(x)

#Order by
sql="SELECT * FROM customers ORDER BY name"
cursor.execute(sql)
myresult = cursor.fetchall()
type(myresult)
for x in myresult:
    print(x)

#DELETE
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
cursor.execute(sql)
db.commit()
print(cursor.rowcount, "record(s) deleted")

#Injection
sql="DELETE FROM customers WHERE address=%s"
adr=("Yellow Garden 2",)
cursor.execute(sql, adr)
db.commit()
print(cursor.rowcount, "record(s) deleted")

#Drop table
sql="DROP TABLE customers"
cursor.execute(sql)
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)

#Drop only if exist
sql="DROP TABLE IF EXISTS customers"
cursor.execute(sql)

#update table
sql="UPDATE customers SET address='Canyon 123' WHERE address='Valley 345'"
cursor.execute(sql)
db.commit()
print(cursor.rowcount, "record(s) affected")

sql="UPDATE customers SET address=%s WHERE address=%s"
val=("Valley 345", "Canyon 123")
cursor.execute(sql, val)
db.commit()
print(cursor.rowcount,"record(s) affected")

# LIMIT the result
cursor.execute("SELECT * FROM customers LIMIT 5")
myresult = cursor.fetchall()
for x in myresult:
    print(x)
cursor.execute("SELECT * FROM customers LIMIT 2, 5")
myresult = cursor.fetchall()
for x in myresult:
    print(x)
#start from position3 and return 5 records
cursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = cursor.fetchall()
for x in myresult:
    print(x)

#JOIN
sql="SELECT users.name as user, products.name as favorite FROM users JOIN products ON users.fav=products.id"
cursor.execute(sql)
myresult=cursor.fetchall()
for x in myresult:
    print(x)
