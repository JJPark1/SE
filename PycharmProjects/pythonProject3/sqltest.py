import pymysql

conn = pymysql.connect(host = 'localhost', user = 'root',password = 'y5154126', db ='university', charset = 'utf8mb4')

cursor = conn.cursor()



sql= """create table student(
    sno char(7) NOT NULL,
    sname varchar(20) NOT NULL,
    grade int DEFAULT 1,
    dept varchar(20),
    primary key(sno))"""

cursor.execute(sql)

while True:
    sno = input("학번: ")
    if sno == "":
        break
    sname = input("이름: ")
    grade = input("학년: ")
    dept = input("학과: ")
    sql = "insert into student values('" + sno + "','" + sname + \
          "','" + grade + "','" + dept + "')"
try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()


cursor.execute("select * from student")
rows = cursor.fetchall()
for cur_row in rows:
    sno = cur_row[0]
    sname = cur_row[1]
    grade = cur_row[2]
    dept = cur_row[3]
    print("%7s %20s %5d %20s" % (sno, sname, grade, dept))

conn.close()