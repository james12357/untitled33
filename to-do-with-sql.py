import pymysql
import time
autoSave = True
conn = pymysql.connect(host='localhost', user="root", passwd="123456", db="testdb")
cursor = conn.cursor()
cursor.execute("USE testdb")
while True:
    r = input("READY>")
    if r == "list":
        cursor.execute("SELECT * FROM TBTEST_1")
        for x in cursor:
            print(x)
    if r == "add":
        cursor.execute("SELECT * FROM TBTEST_1")
        cursor.execute("INSERT INTO TBTEST_1 (todo, date) values(%s,%s)", (" " + input("?>"), time.asctime(time.localtime(time.time()))))
        if autoSave:
            conn.commit()
    if r == "save":
        conn.commit()
    if r == "del":
        cursor.execute("DELETE FROM TBTEST_1 WHERE todo = '"+input("?>")+"'")
        if autoSave:
            conn.commit()
