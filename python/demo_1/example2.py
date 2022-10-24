# coding:utf-8

import mysql.connector

# 連接
con = mysql.connector.connect(
    host='localhost', port='3306',
    user='root', password='tony1120',
    database='vega'
)

# 因為或關係 和 後方必定為真, 所以語句必定為真
username='1 OR 1=1'
password='1 OR 1=1'
'''
sql = 'SELECT COUNT(*) FROM t_user WHERE username='+username+\
    ' AND AES_DECRYPT(UNHEX(password), "HelloWorld")='+password;
'''
sql = 'SELECT COUNT(*) FROM t_user WHERE username=%s'\
    ' AND AES_DECRYPT(UNHEX(password), "HelloWorld")=%s';

cursor = con.cursor()
cursor.execute(sql, (username, password))
print(cursor.fetchone()[0])

con.close()