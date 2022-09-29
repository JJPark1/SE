import pymysql


conn = pymysql.connect(host='localhost', user='root', password='root', db='appliance_rental', charset='utf8mb4')

cursor = conn.cursor()
cursor.execute("set foreign_key_checks = 0")

cursor.execute("drop table IF EXISTS 고객")

sql = """create table 고객 (
    CID char(5) NOT NULL,
    cname varchar(5),
    contact varchar(20),
    primary key(CID))"""
cursor.execute(sql)

cursor.execute("drop table IF EXISTS 대리점")

sql = """create table 대리점 (
    BID char(4) NOT NULL,
    대리점이름 varchar(10),
    baddress varchar(20),
    primary key(BID))"""
cursor.execute(sql)


cursor.execute("drop table IF EXISTS 제품모델")
sql = """create table 제품모델 (
    BID char(4) not null,
    모델번호 char(4) not null,
    종류  varchar(10),
    CID char(5),
    렌탈예정일 date,    
    primary key(BID,모델번호),
    foreign key(BID) references 대리점(BID) on delete cascade,
    foreign key(CID) references 고객(CID) on delete cascade)"""
cursor.execute(sql)

cursor.execute("set foreign_key_checks = 1")
global login_id

def join(cursor) :

    line = r_file.readline()
    line = line.strip()
    column_values = line.split()
    CID = column_values[0]
    cname = column_values[1]
    contact = column_values[2]

    sql = "insert into 고객 values('" + CID + "','" + cname + "','" + contact + "')"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    # 출력 형식
    w_file.write("1.1. 회원가입\n")
    w_file.write("> " + CID + ' ' + cname + ' ' + contact + "\n")
def exit() :
    w_file.write("1.2. 종료\n")

def c_login(cursor):
    global login_id
    line = r_file.readline()
    line = line.strip()
    column_values = line.split()
    CID = column_values[0]
    login_id = CID
    w_file.write("2.1. 로그인\n")
    w_file.write("> "+ CID +"\n")


def reserve(cursor):
    line = r_file.readline()
    line = line.strip()
    column_values = line.split()
    BID = column_values[0]
    모델번호 = column_values[1]
    렌탈예정일 = column_values[2]

    sql= "UPDATE 제품모델 SET CID= "+"'"+login_id+"'" + " WHERE 모델번호 ="+"'"+모델번호+"' AND BID ="+"'"+BID+"'"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    sql= "UPDATE 제품모델 SET 렌탈예정일= "+"'"+ 렌탈예정일 + "'" + " WHERE 모델번호 ="+"'"+모델번호+"' AND BID ="+"'"+BID+"'"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    cursor.execute("select * from 제품모델 where 모델번호 ="+"'"+모델번호+"' AND BID="+"'"+BID+"'")
    rows = cursor.fetchall()
    for cur_row in rows:
        BID = cur_row[0]
        모델번호 = cur_row[1]
        종류 = cur_row[2]
        렌탈예정일 = cur_row[4]
        w_file.write("2.2. 제품 렌탈 예약\n")
        w_file.write("> " + BID + ' ' + 모델번호 + ' ' + 종류 + ' ' + str(렌탈예정일) + "\n")

def print_(cursor):
    sql = "select 제품모델.BID,제품모델.모델번호,제품모델.종류,제품모델.렌탈예정일 " \
          "from 고객,제품모델 WHERE 고객.CID = 제품모델.CID AND 고객.CID = '" + login_id + "'"
    cursor.execute(sql)
    rows = cursor.fetchall()
    w_file.write("2.3. 제품 렌탈 예약 조회\n")
    for cur_row in rows:
        BID = cur_row[0]
        모델번호 = cur_row[1]
        종류 = cur_row[2]
        렌탈예정일 = cur_row[3]
        w_file.write("> " + BID + ' ' + 모델번호 + ' ' + 종류 + ' ' + str(렌탈예정일) + "\n")
def cancel(cursor):
    line = r_file.readline()
    line = line.strip()
    column_values = line.split()

    BID = column_values[0]
    모델번호 = column_values[1]
    sql = "select 제품모델.BID,제품모델.모델번호,제품모델.종류,제품모델.렌탈예정일 from 고객,제품모델 " \
          "WHERE 고객.CID = 제품모델.CID AND BID ="+"'" + BID + "'" + " AND 모델번호 = " + "'" + 모델번호 + "'"
    cursor.execute(sql)
    rows = cursor.fetchall()
    w_file.write("2.4. 제품 렌탈 예약 취소\n")
    for cur_row in rows:
        BID = cur_row[0]
        모델번호 = cur_row[1]
        종류 = cur_row[2]
        렌탈예정일 = cur_row[3]
        w_file.write("> " + BID + ' ' + 모델번호 + ' ' + 종류 + ' ' + str(렌탈예정일) + "\n")
    sql = "UPDATE 제품모델 SET 렌탈예정일= " + "NULL" + " WHERE 모델번호 =" + "'" + 모델번호 + "' AND BID =" + "'" + BID + "'"
    try:
        cursor.execute(sql)

        conn.commit()
    except:
        conn.rollback()
    sql = "UPDATE 제품모델 SET CID= " + "NULL" + " WHERE 모델번호 =" + "'" + 모델번호 + "' AND BID =" + "'" + BID + "'"
    try:
        cursor.execute(sql)

        conn.commit()
    except:
        conn.rollback()

def c_logout():
    global login_id
    w_file.write("2.5. 로그아웃\n")
    w_file.write("> " + login_id + "\n")
    login_id = "NULL"

def a_login(cursor):
    global login_id
    line = r_file.readline()
    line = line.strip()
    column_values = line.split()
    CID = column_values[0]

    login_id = CID

    w_file.write("3.1. 로그인\n")
    w_file.write("> "+ CID +"\n")

def b_apply(cursor):
    line = r_file.readline()
    line = line.strip()
    column_values = line.split()
    BID = column_values[0]
    대리점이름 = column_values[1]
    baddress = column_values[2]

    sql = "insert into 대리점 values('" + BID + "','" + 대리점이름 + "','" + baddress + "')"
    try:
        cursor.execute(sql)

        conn.commit()
    except:
        conn.rollback()


    # 출력 형식
    w_file.write("3.2. 대리점 정보 등록\n")
    w_file.write("> " + BID + ' ' + 대리점이름 + ' ' + baddress + "\n")




def m_apply(curosr):
    line = r_file.readline()
    line = line.strip()
    column_values = line.split()
    BID = column_values[0]
    모델번호 = column_values[1]
    종류 = column_values[2]
    sql = "insert into 제품모델 values('" + BID + "','" + 모델번호 + "','" + 종류 + "'," + "NULL" + "," + "NULL" + ")"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    w_file.write("3.3. 제품 정보 등록\n")
    w_file.write("> " + BID + ' ' + 모델번호 + ' ' + 종류 + "\n")




def print_all(cursor):
    sql="""select 고객.cname,제품모델.CID,제품모델.BID,제품모델.모델번호,제품모델.종류,제품모델.렌탈예정일
     from 고객,제품모델 WHERE 고객.CID = 제품모델.CID"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    w_file.write("3.4. 렌탈 예약 내역 전체 조회\n")
    for cur_row in rows:
        cname= cur_row[0]
        CID=cur_row[1]
        BID = cur_row[2]
        모델번호 = cur_row[3]
        종류 = cur_row[4]
        렌탈예정일 = cur_row[5]
        w_file.write("> " + cname +' ' + CID + ' '+ BID + ' ' + 모델번호 + ' ' + 종류  +' ' + str(렌탈예정일) + "\n")
def print_mno(cursor):
    line = r_file.readline()
    line = line.strip()
    column_values = line.split()
    mno_input = column_values[0]

    if len(mno_input)==1:
        sql = "select 고객.cname,제품모델.CID,제품모델.BID,제품모델.모델번호,제품모델.종류,제품모델.렌탈예정일 " \
              "from 고객,제품모델 WHERE 고객.CID = 제품모델.CID AND 모델번호 LIKE " + "'%" + mno_input + "%'"
        cursor.execute(sql)

    elif len(mno_input)==2:
        sql = "select 고객.cname,제품모델.CID,제품모델.BID,제품모델.모델번호,제품모델.종류,제품모델.렌탈예정일 " \
              "from 고객,제품모델 WHERE 고객.CID = 제품모델.CID AND 모델번호 LIKE " + "'%" + mno_input[0] + "%' AND 모델번호 LIKe '%" + mno_input[1] + "%'"
        cursor.execute(sql)
    elif len(mno_input)==3:
        sql = "select 고객.cname,제품모델.CID,제품모델.BID,제품모델.모델번호,제품모델.종류,제품모델.렌탈예정일 " \
              "from 고객,제품모델 WHERE 고객.CID = 제품모델.CID AND 모델번호 LIKE " + "'%" + mno_input[0] + "%' AND 모델번호 LIKe '%" + \
              mno_input[1] + "%' AND 모델번호 LIKE '%"+ mno_input[2]+"%'"
        cursor.execute(sql)
    elif len(mno_input)==4:
        sql = "select 고객.cname,제품모델.CID,제품모델.BID,제품모델.모델번호,제품모델.종류,제품모델.렌탈예정일 " \
            "from 고객,제품모델 WHERE 고객.CID = 제품모델.CID AND 모델번호 LIKE '%" + mno_input + "%'"
        cursor.execute(sql)

    rows = cursor.fetchall()
    w_file.write("3.5. 렌탈 예약 내역 조회 (모델번호)\n")
    for cur_row in rows:
        cname= cur_row[0]
        CID=cur_row[1]
        BID = cur_row[2]
        모델번호 = cur_row[3]
        종류 = cur_row[4]
        렌탈예정일 = cur_row[5]
        w_file.write("> " + cname +' ' + CID + ' '+ BID + ' ' + 모델번호 + ' ' + 종류  +' ' + str(렌탈예정일) + "\n")
def print_cid(cursor):
    line = r_file.readline()
    line = line.strip()
    column_values = line.split()
    cid_cname = column_values[0]

    if len(cid_cname)==1:
        sql = "select 고객.cname,제품모델.CID,제품모델.BID,제품모델.모델번호,제품모델.종류,제품모델.렌탈예정일 from 고객,제품모델 " \
              "WHERE 고객.CID = 제품모델.CID AND 고객.cname LIKE " + "'%" + cid_cname[0] + "%'"
        cursor.execute(sql)

    elif len(cid_cname)==2:
        sql = "select 고객.cname,제품모델.CID,제품모델.BID,제품모델.모델번호,제품모델.종류,제품모델.렌탈예정일 from 고객,제품모델 " \
              "WHERE 고객.CID = 제품모델.CID AND 고객.cname LIKE "+"'%"+ cid_cname[0] +"%' AND 고객.cname LIKE '%" +cid_cname[1] + "%'"
        cursor.execute(sql)

    elif len(cid_cname)==3:
        sql = "select 고객.cname,제품모델.CID,제품모델.BID,제품모델.모델번호,제품모델.종류,제품모델.렌탈예정일 from 고객,제품모델 " \
              "WHERE 고객.CID = 제품모델.CID AND 고객.cname LIKE " + "'%" + cid_cname + "%'"
        cursor.execute(sql)


    rows = cursor.fetchall()
    w_file.write("3.6. 렌탈 예약 내역 조회 (고객 이름)\n")
    for cur_row in rows:
        cname= cur_row[0]
        CID=cur_row[1]
        BID = cur_row[2]
        모델번호 = cur_row[3]
        종류 = cur_row[4]
        렌탈예정일 = cur_row[5]
        w_file.write("> " + cname +' ' + CID + ' '+ BID + ' ' + 모델번호 + ' ' + 종류  +' ' + str(렌탈예정일) + "\n")
def a_logout():
    global login_id
    w_file.write("3.7. 로그아웃\n")
    w_file.write("> " + login_id + "\n")
    login_id = "NULL"

def doTask() :

    # 종료 메뉴(1 2)가 입력되기 전까지 반복함
    while True :
        # 입력파일에서 메뉴 숫자 2개 읽기
        line = r_file.readline()
        line = line.strip()
        menu_levels = line.split()

        # 메뉴 파싱을 위한 level 구분
        menu_level_1 = int(menu_levels[0])
        menu_level_2 = int(menu_levels[1])

        # 메뉴 구분 및 해당 연산 수행
        if menu_level_1 == 1:
            if menu_level_2 == 1:
                join(cursor)
            elif menu_level_2 == 2:
                exit()
                break
        elif menu_level_1 == 2:
            if menu_level_2 == 1:
                c_login(cursor)
            elif menu_level_2==2:
                reserve(cursor)
            elif menu_level_2==3:
                print_(cursor)
            elif menu_level_2 == 4:
                cancel(cursor)
            elif menu_level_2 == 5:
                c_logout()
        elif menu_level_1 == 3:
            if menu_level_2 == 1:
                a_login(cursor)
            elif menu_level_2 == 2:
                b_apply(cursor)
            elif menu_level_2 == 3:
                m_apply(cursor)
            elif menu_level_2 == 4:
                print_all(cursor)
            elif menu_level_2 == 5:
                print_mno(cursor)
            elif menu_level_2 == 6:
                print_cid(cursor)
            elif menu_level_2 == 7:
                a_logout()

##############
#  메인 코드  #
##############

r_file = open("input.txt","r")
w_file = open("output.txt","w")

doTask()

r_file.close()
w_file.close()





cursor.execute("drop table 제품모델 cascade")
cursor.execute("drop table 고객 cascade")
cursor.execute("drop table 대리점 cascade")

conn.close()
