"""
a=1
b=2
c=3
d=4
e=5
"""
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter as Cot
import pymysql
conn = pymysql.connect(host=input("host>"), user=input("user>"), passwd=input("passwd>"), db=input("[testdb] db>"))
cursor = conn.cursor()
while True:
    inp = input(">")
    while inp == "inp":
        u = input("h>")
        j = []
        if len(u) == 5:
            for i in u:
                j.append(int(i))
            print(j)
            cursor.execute("INSERT INTO COMP (a,b,c,d,e) values(%s,%s,%s,%s,%s)", tuple(j))
            conn.commit()
    if inp == "show":
        j = []
        cursor.execute("select " + input(">") + " from comp;")
        for i in cursor:
            j.append(i[0])
        res = Cot(j)
        for i in list("12345"):
            if not res[int(i)]:
                res[int(i)] = 0
        x = np.array(["1", "2", "3", "4", "5"])
        y = np.array([res[1], res[2], res[3], res[4], res[5]])
        plt.bar(x, y)
        plt.show()
