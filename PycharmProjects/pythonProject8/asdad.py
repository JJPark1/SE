import pymysql

conn = pymysql.connect(host = 'localhost', user = 'root',password = 'y5154126', db ='test1', charset = 'utf8mb4')

cursor = conn.cursor()

cursor.execute("drop table IF EXISTS student")

sql= """create table student (
    sno char(7) NOT NULL,
    sname varchar(20) NOT NULL,
    grade int DEFAULT 1,
    dept varchar(20),
    primary key(sno))"""
cursor.execute(sql)


cursor.execute("drop table IF EXISTS course")

sql= """create table course (
    cno char(4) NOT NULL,
    cname varchar(30) NOT NULL,
    credit int ,
    profname char(20),
    dept varchar(20),
    primary key(cno))"""

cursor.execute(sql)


def insert_student(cursor):
    sql = """insert into student
        values('B823019', '홍길동', 4, '컴퓨터')"""
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    sql = """insert into student
           values('B890515', '김철수', 3, '전기')"""
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

def insert_course(cursor):
    sql = """insert into course
           values('C101', '전기회로', 3, '김홍익','전기')"""
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    sql = """insert into course
           values('C102', '데이터베이스', 4, '이대학','컴퓨터')"""
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()


def search_course(cursor):
    cursor.execute("select * from course")
    rows = cursor.fetchall()
    for cur_row in rows:
        cno = cur_row[0]
        cname = cur_row[1]
        credit = cur_row[2]
        profname = cur_row[3]
        dept = cur_row[4]
        print("%s %s %5d %s %s" % (cno, cname, credit, profname,dept))





def search_student(cursor):
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    for cur_row in rows:
        sno = cur_row[0]
        sname = cur_row[1]
        grade = cur_row[2]
        dept = cur_row[3]
        print("%s %s %5d %s" % (sno, sname, grade, dept))




while 1:

    print("0. 종료")
    print("1.student 레코드 검색")
    print("2.course 레코드 검색")
    print("기능을 선택하시오: ")
    a = int(input())

    if a==1:
        insert_student(cursor)
        search_student(cursor)

    elif a==2:
        insert_course(cursor)
        search_course(cursor)
    elif a==0:
        break
    print("\n")

conn.close()
