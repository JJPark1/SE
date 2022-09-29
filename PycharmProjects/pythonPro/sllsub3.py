import pymysql

conn = pymysql.connect(host='localhost', user='root', password='y5154126', db='te1117', charset='utf8mb4')

cursor = conn.cursor()
cursor.execute("drop table IF EXISTS employee")
sql = """create table employee (
    eno char(8) NOT NULL,
    ename varchar(30) ,
    years int ,
    address varchar(50),
    contact varchar(20),
    primary key(eno))"""

cursor.execute(sql)

def create_record(cursor):
    n = int(input("- 생성할 레코드 수를 입력하시오 :"))
    eno="E1"
    ename = eno + eno

    for i in range(0,n):
        sql = "insert into employee values('"+eno+"','"+ename+"',"+"NULL"+","+"NULL"+","+"NULL"+")"
        try:
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        temp1=eno[0:1]
        temp2=eno[1:]
        temp3=int(temp2)
        temp3+=1
        temp2=str(temp3)
        eno = temp1 + temp2
        ename = eno + eno

def create_index(cursor):
    n = input("- 생성할 인덱스 속성을 입력하시오 :")
    sql = "create index ix_"+n+" on employee ("+n+")"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

def delete_index(cursor):
    n = input("- 삭제할 인덱스 속성을 입력하시오 :")
    sql = "drop index ix_"+n+" on employee"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()


while 1:
    print("0. 종료")
    print("1. 레코드 생성")
    print("2. 인덱스 생성")
    print("3. 인덱스 삭제")
    a = int(input("기능을 선택하시오: "))
    if a == 1:
        create_record(cursor)
    elif a == 2:
        create_index(cursor)
    elif a == 0:
        break
    elif a == 3:
        delete_index(cursor)
    print("\n")

conn.close()