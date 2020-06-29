import pymysql
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user='eprot',
    passwd='1234',
    db='mydb'
)

cursor=conn.cursor()
sql="INSERT INTO books VALUES(:title, :url)"
val={"title":"hihi", "url":"1234"}
cursor.execute(sql,val)

conn.commit()
