import pymysql
import random
conn = pymysql.connect(host="localhost", user="root", passwd="123456", db="testdb")
cursor = conn.cursor()
cursor.execute("USE testdb")
for i in range(200000):
    cursor.execute("INSERT INTO TEST (a, b, c) values(%s,%s,%s)", (random.randint(1, 1000000), random.randint(1, 1000000), random.randint(1, 1000000)))
conn.commit()
