import pymysql.cursors
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    db='test',
    charset='utf8'
)

cursor=connect.cursor()
sql="select * from trade"
cursor.execute(sql)
for i in cursor.fetchall():
    print((i))