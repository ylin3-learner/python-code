# coding:utf-8

import mysql.connector

# 創建連接1
con = mysql.connector.connect(
    host='localhost', port='3306',
    user='root', password='tony1120',
    database='demo',
)



# 創建連接2
'''
config = {
    "host": 'localhost',
    "port": 3306,
    "user": 'root',
    'password': 'tony1120',
    'database': 'demo'
}

con = mysql.connector.connect(**config)
'''
cursor = con.cursor()

sql='SELECT empno, ename, hiredate FROM t_emp'
cursor.execute(sql)
for one in cursor:
    print(one[0], one[1], one[2])

con.close()