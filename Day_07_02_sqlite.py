import sqlite3
import Day_05_02_csv
def createDB(filename):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute('Drop Table If Exists kma')
    conn.commit()
    query = 'CREATE TABLE if not exists kma (prov text, city text, mode text, tmEf text, wf text, tmn text, tmx text, reli text)'
    cur.execute(query)
    # cur.execute('Drop Table If Exists new_table')

    conn.commit()
    conn.close()

# def insertSingle(filename, row):
#     conn = sqlite3.connect(filename)
#     cur = conn.cursor()
#
#     # insert
#     # into
#     # 테이블명(필드1, 필드2, ·······) values(값1, 값2, ·······)
#     base = 'INSERT INTO kma VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
#     query = base.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
#     cur.execute(query)
#
#     conn.commit()
#     conn.close()

def insertAll(filename, rows):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    base = 'INSERT INTO kma VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
    for row in rows:
        query = base.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        cur.execute(query)
    conn.commit()
    conn.close()

def fetch(filename):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    query = 'SELECT * FROM kma'
    rows = cur.execute(query)
    print(*rows, sep='\n')

    conn.commit()
    conn.close()

def fetchWhere(filename, city):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    query = 'SELECT * FROM kma WHERE city = "{}"'.format(city)
    rows = cur.execute(query)
    print(*rows, sep='\n')

    conn.commit()
    conn.close()
# select * from creature_template where name = '일리단 스톰레이지';

filename = 'Data/kma.sqlite'
createDB(filename)
rows = Day_05_02_csv.read_2('Data/kma.csv')

insertAll(filename, rows)
a = input("찾고싶은 도시 이름 : ")
fetchWhere(filename, a)








