import pymysql

conn = pymysql.connect(host='localhost',user='root',password='y5154126',db='university',charset='utf8mb4')

curs = conn.cursor()

sql="select * from student"
curs.execute(sql)

rows= curs.fetchall()
print(rows)

conn.close()