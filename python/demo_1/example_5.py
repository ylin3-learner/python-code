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
    # con.start_transaction()
    cursor = con.cursor()
    # sql = 'DELETE e, d FROM t_emp e JOIN t_dept d ON e.deptno=d.deptno AND d.deptno=20'
    sql = 'TRUNCATE table t_emp'  # TRUNCATE 是在事務機制之外的, 因此需要把涉及事務的代碼註釋掉
    # truncate table t_emp == delete from t_emp
    cursor.execute(sql)
    # con.commit()
except Exception as e:
    # if 'con' in dir():
    #     con.rollback()
    print(e)