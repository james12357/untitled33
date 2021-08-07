import pymysql
import time
autoSave = True
conn = pymysql.connect(host=input("host>"), user=input("user>"), passwd=input("passwd>"), db=input("[testdb] db>"))
cursor = conn.cursor()
cursor.execute("USE testdb")

while True:
    try:
        r = input("READY>")
        r = r.split(" ", 1)
        if r[0] == "list":
            cursor.execute("SELECT * FROM LST")
            for x in cursor:
                print(x)
        if r[0] == "add":
            # noinspection PyTypeChecker
            r[1] = r[1].split(" ", 1)
            cursor.execute("SELECT * FROM LST")
            cursor.execute("INSERT INTO LST (title, content, date) values(%s,%s,%s)", (r[1][0], r[1][1], time.asctime(time.localtime(time.time()))))
            if autoSave:
                conn.commit()
        if r[0] == "save":
            print("changes saved.")
            conn.commit()
        if r[0] == "del":
            cursor.execute("DELETE FROM LST WHERE title = '"+r[1]+"'")
            if autoSave:
                conn.commit()
        if r[0] == "drop":
            cursor.execute("DELETE FROM LST WHERE title like  '%"+r[1]+"%'")
            print("Drop method will not save changes until you decided.\nRun 'save' to save changes.")
        if r[0] == "find":
            # noinspection PyTypeChecker
            r[1] = r[1].split(" ", 1)
            if r[1][0] == "title":
                cursor.execute("SELECT * FROM LST WHERE title like '%"+r[1][1]+"%';")
                for x in cursor:
                    print(x)
            if r[1][0] == "content":
                cursor.execute("SELECT * FROM LST WHERE content like '%"+r[1][1]+"%';")
                for x in cursor:
                    print(x)
            if r[1][0] == "id":
                cursor.execute("SELECT * FROM LST WHERE id like '%"+r[1][1]+"%';")
                for x in cursor:
                    print(x)
            """cursor.execute("SELECT * FROM LST WHERE title like '%"+r[1]+"%';")
            for x in cursor:
                print(x)"""

        if r[0] == "select":
            # noinspection PyTypeChecker
            r[1] = r[1].split(" ", 1)
            if r[1][0] == "top":
                cursor.execute("SELECT * from lst order by id limit " + r[1][1])
                for x in cursor:
                    print(x)
            if r[1][0] == "last":
                cursor.execute("SELECT * from lst order by id desc limit " + r[1][1])
                for x in cursor:
                    print(x)

    except IndexError:
        print("Error:too few arguments")

