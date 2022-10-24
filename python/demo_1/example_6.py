# coding:utf-8

import mysql.connector.pooling

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'tony1120',
    'database': 'demo'
}

pool = mysql.connector.pooling.MySQLConnectionPool(
    **config,
    pool_size=10
)

try:
    con = pool.get_connection()
    con.start_transaction()
    cursor = con.cursor()
    sql = 'INSERT INTO t_dept(deptno, dname, loc) VALUES (%s, %s, %s)'
    data = [
        [100, 'A部門', '北京'], [200, 'B部門', '上海']
    ]
    cursor.executemany(sql, data)  # 執行sql多次
    con.commit()
except Exception as e:
    if 'con' in dir():
        con.rollback()
    print(e)
