import pymysql
import time
autoSave = True
conn = pymysql.connect(host='localhost', user="root", passwd="123456", db="testdb")
cursor = conn.cursor()
cursor.execute("USE testdb")

while True:
    try:
        r = input("READY>")
        r = r.split(" ", 1)
        if r[0] == "list":
            cursor.execute("SELECT * FROM TBTEST_1")
            for x in cursor:
                print(x)
        if r[0] == "add":
            cursor.execute("SELECT * FROM TBTEST_1")
            cursor.execute("INSERT INTO TBTEST_1 (todo, date) values(%s,%s)", (r[1], time.asctime(time.localtime(time.time()))))
            if autoSave:
                conn.commit()
        if r[0] == "save":
            conn.commit()
        if r[0] == "del":
            cursor.execute("DELETE FROM TBTEST_1 WHERE todo = '"+r[1]+"'")
            if autoSave:
                conn.commit()
        if r[0] == "drop":
            cursor.execute("DELETE FROM TBTEST_1 WHERE todo like  '%"+r[1]+"%'")
            print("Drop method will not automatically save.\nRun 'save' to save changes.")
        if r[0] == "find":
            cursor.execute("SELECT * FROM tbtest_1 where todo like '%"+r[1]+"%';")
            for x in cursor:
                print(x)
    except IndexError:
        print("Error:too few arguments")

