# coding:utf-8

# 編寫一個INSERT語句向部門表插入兩條紀錄
# 每條紀錄都在部門原有最大主鍵值MAX(deptno)的基礎上+10
'''
錯誤SQL: INSERT INTO t_dept(deptno, dname, loc) VALUES(SELECT MAX(deptno) FROM t_dept)+10, 'A部門', '北京'))
因為不能同時插入數據與查詢數據都為同一張表, 造成無盡地數據被插入
'''
# 改進：將想要查詢並插入的數據直接變成一張結果集, 直接插入部門表 -> 先查詢, 在插入
# INSERT INTO t_dept(SELECT MAX(deptno)+10, 'A部門', '北京' FROM t_dept)

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

# 事實上，就算不開啟事務機制也可以執行sql, 可是如果強制開啟事務機制就會將所有sql視為整體, 因為原子性
try:
    con = pool.get_connection()
    con.start_transaction()
    cursor = con.cursor()
    sql = 'INSERT INTO t_dept(deptno, dname, loc) VALUES('\
    'SELECT MAX(deptno)+10, %s, %s FROM t_dept'\
    'SELECT MAX(deptno)+20, %s, %s FROM t_dept'
    sql += ')'
    print(sql)
    cursor.execute(sql, ('A部門', '北京', 'B部門', '上海'))
    con.commit()
except Exception as e:
    if 'con' in dir():
        con.rollback()

