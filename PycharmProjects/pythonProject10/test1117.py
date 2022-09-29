import pymysql

conn = pymysql.connect(host='localhost', user='root', password='y5154126', db='te1117', charset='utf8mb4')

cursor = conn.cursor()
cursor.execute("set foreign_key_checks = 0")

cursor.execute("drop table IF EXISTS student")

sql = """create table student (
    sno char(7) NOT NULL,
    sname varchar(20) NOT NULL,
    grade int DEFAULT 1,
    dept varchar(20),
    primary key(sno))"""
cursor.execute(sql)

cursor.execute("drop table IF EXISTS course")

sql = """create table course (
    cno char(4) NOT NULL,
    cname varchar(30) NOT NULL,
    credit int ,
    profname char(20),
    dept varchar(20),
    primary key(cno))"""

cursor.execute(sql)

cursor.execute("drop table IF EXISTS enroll")

sql = """create table enroll (
    sno char(7) NOT NULL,
    cno char(4) NOT NULL,
    final char(2) ,
    lettergrade char(2),

  
    foreign key(sno) references student(sno) on delete cascade,
    foreign key(cno) references course(cno) on delete cascade,
    primary key(sno,cno))"""
cursor.execute(sql)

cursor.execute("set foreign_key_checks = 1")

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


def insert_enroll(curosr):
    sno = input("학번을 입력하시오: ")
    cno = input("과목번호를 입력하시오: ")
    final = input("기말고사 점수를 입력하시오: ")
    lettergrade = input("학점을 입력하시오: ")
    sql = "insert into enroll values('" + sno + "','" + cno + \
          "', " + final + ", '" + lettergrade + "')"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()


def search_course(cursor):
    cursor.execute("select * from course")
    rows = cursor.fetchall()
    print("%-4s %-30s %5s %-20s %-20s" % ("cno", "cname", "credit", "profname", "dept"))
    for cur_row in rows:
        cno = cur_row[0]
        cname = cur_row[1]
        credit = cur_row[2]
        profname = cur_row[3]
        dept = cur_row[4]
        print("%-4s %-30s %5s %-20s %-20s" % (cno, cname, credit, profname, dept))


def search_student(cursor):
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    print("%-7s %-20s %5s %-20s" % ("sno", "sname", "grade", "dept"))
    for cur_row in rows:
        sno = cur_row[0]
        sname = cur_row[1]
        grade = cur_row[2]
        dept = cur_row[3]
        print("%-7s %-20s %5s %-20s" % (sno, sname, grade, dept))


def search_enroll(curosr):
    cursor.execute("select * from enroll")
    rows = cursor.fetchall()
    print("%-7s %-20s %5s %-20s" % ("sno", "cno", "final", "lettergrade"))
    for cur_row in rows:
        sno = cur_row[0]
        cno = cur_row[1]
        final = cur_row[2]
        lettergrade = cur_row[3]
        print("%-7s %-20s %5s %-20s" % (sno, cno, final, lettergrade))


insert_student(cursor)
insert_course(cursor)

while 1:

    print("0. 종료")
    print("1.student 레코드 검색")
    print("2.course 레코드 검색")
    print("3.enroll 레코드 검색")
    print("4.enroll 레코드 삽입")
    print("기능을 선택하시오: ")
    a = int(input())

    if a == 1:
        search_student(cursor)
    elif a == 2:
        search_course(cursor)
    elif a == 0:
        break
    elif a == 4:
        insert_enroll(cursor)
    elif a == 3:
        search_enroll(cursor)
    print("\n")

conn.close()