# coding:utf-8

import mysql.connector.pooling

'''
config = mysql.connector.connect(
    host='localhost', port=3306,
    user='root', password='tony1120',
    database='demo'
)
'''
# 以上代碼是直接連接，而不是先建立參數在傳參至連接池

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'tony1120',
    'database': 'demo'
}
# 連接：pool.get_connection()
# 如果需要增刪改, 就需要事務機制 -> 將連接結果調用並使用start_transaction()
# 如果預先創建連接池連接，就可以避免反覆創建和銷毀的昂貴代價
try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=30
    )
    con = pool.get_connection()
    con.start_transaction()
    cursor = con.cursor()
    sql = "UPDATE t_emp SET sal=sal+%s WHERE deptno=%s"
    cursor.execute(sql, (200, 20))
# 餐数sql后的参数是个元组类型，单个数据的元组数据后面加逗号
    con.commit()
    print(dir(cursor.fetchone()))  # 由此可知，cursor.fetchone返回的是對象
    print(dir(cursor.fetchall()))  # 由此可知，cursor.fetchone返回的是對象
except Exception as e:
    if 'con' in dir():
        con.rollback()
    print(e)