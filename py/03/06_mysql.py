import pymysql
conn = pymysql.connect(
    db="scraping",
    user='scraper',
    passwd='1234',
    charset='utf8mb4'
)

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS cities")
c.execute('''
    CREATE TABLE cities(
    rank int,
    city text,
    population int)''')

c.execute("INSERT INTO cities VALUES(%s, %s, %s)", (1,"상하이",24150000))

sql="INSERT INTO cities VALUES(%(rank)s, %(city)s, %(population)s)"
val={"rank":2,"city":"카라치","population":23500000}
c.execute(sql,val)

sql="INSERT INTO cities VALUES(%(rank)s, %(city)s, %(population)s)"
val=[{"rank":3,"city":"베이징","population":21516000},
     {"rank":4,"city":"텐진","population":14722100},
     {"rank":5,"city":"이스탄불","population":14160467}]
c.executemany(sql, val)
conn.commit()

c.execute("SELECT * FROM cities")
for row in c.fetchall():
    print(row)
conn.close()