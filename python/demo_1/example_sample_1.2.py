# coding:utf-8

# 分解sql語句
# 使用INSERT語句，把部門平均底薪超過公司部門底薪的這樣部門裡的
# 員工信息導入到t_emp_new表裡面，並且讓這些員工隸屬於SALES部門

# 創建數據池, 連接, 支持事務機制與回滾

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

    # 使用INSERT語句，把部門平均底薪超過公司部門底薪的這樣部門裡的
    # 員工信息導入到t_emp_new表裡面，並且讓這些員工隸屬於SALES部門

    # 創建t_emp_new表有t_emp的結構
    sql_1 = 'CREATE TABLE t_emp_new LIKE t_emp'
    cursor.execute(sql_1)

    # 公司平均底薪
    sql_2 ='SELECT AVG(sal) AS avg FROM t_emp'
    cursor.execute(sql_2)
    temp = cursor.fetchone()  # 獲得資料非純數據, 而是'decimal.Decimal' object
    avg = temp[0]
    sql_3 = 'SELECT deptno FROM t_emp GROUP BY deptno HAVING AVG(sal) >= %s'
    cursor.execute(sql_3, (avg,))

    temp = cursor.fetchall()  # cursor.fetchall()返回列表型式
    print(temp)
    print(dir(cursor.fetchone()))  # 由此可知，cursor.fetchone返回的是對象
    print(dir(cursor.fetchall()))  # 由此可知，cursor.fetchone返回的是對象

    # 插入數據到t_emp_new
    sql_4 = 'INSERT INTO t_emp_new SELECT * FROM t_emp WHERE deptno IN ('
    for index in range(len(temp)):
        department = temp[index][0]
        if index < len(temp) -1:
            sql_4 += str(department) + ','
        else:
            sql_4 += str(department)
    sql_4 += ')'
    cursor.execute(sql_4)
    print(sql_4)

    # 刪除原本在t_emp但移到t_emp_new的資料
    sql = "DELETE FROM t_emp WHERE deptno IN ("
    for i in range(len(temp)):
        num = temp[i][0]
        if i < len(temp) - 1:
            sql += str(num) + ','
        else:
            sql += str(num)
    sql += ")"
    print(sql)
    cursor.execute(sql)

    # 找出原本在t_dept表中SALES部門的編號
    sql_5 = 'SELECT deptno FROM t_dept WHERE dname=%s'
    cursor.execute(sql_5, ['SALES'])
    deptno = cursor.fetchone()[0]
    print(cursor.fetchone())
    print(deptno)

    # 將被遷移到t_emp_new的員工部門改為SALES部門
    sql_6= 'UPDATE t_emp_new SET deptno=%s'
    # execute(sql, (username,))
    # 中第二个参数需要是可迭代数据类型的数据元组或列表，使用元组和列表传参效果都是一样的
    cursor.execute(sql_6, [deptno])
    con.commit()
except Exception as e:
    if 'con' in dir():
        con.close()
    print(e)
