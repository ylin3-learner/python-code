# coding:utf-8

import mysql.connector

try:
    con = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='tony1120',
        database='demo'
    )
    cursor = con.cursor()
    sql = "INSERT INTO t_emp(empno, ename, job, mgr, hiredate, sal, comm, deptno)"\
        "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (9600, '林佑綸', 'ENGINEER', None, '2022-6-16', 2500, None, 10))
    con.commit()
except Exception as e:
    con.rollback()
    print(e)
finally:
    if 'con' in dir():
        con.close()
