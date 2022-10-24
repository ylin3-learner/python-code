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
    # 因為需要插入, 需要開啟事務機制
    con.start_transaction()
    cursor = con.cursor()
    # sql = 'DROP TABLE t_emp_new'
    # cursor.execute(sql)
    sql = 'CREATE TABLE t_emp_new LIKE t_emp'
    # CREATE TABLE t_emp_new AS (SELECT * FROM t_emp)導入t_emp的表到t_emp_new
    # CREATE TABLE t_emp_new LIKE t_emp 導入t_emp的表到t_emp_new
    cursor.execute(sql)

    # 使用INSERT語句，把部門平均底薪超過公司部門底薪的這樣部門裡的
    # 員工信息導入到t_emp_new表裡面，並且讓這些員工隸屬於SALES部門

    sql = 'SELECT AVG(sal) AS avg FROM t_emp'
    cursor.execute(sql)
    temp = cursor.fetchone()  # 抓取全部數據，當數據只有一條 Vs. fetchall() 一次抓取多條紀錄
    # print(temp) -> (Decimal('2073.214286'),)
    avg = temp[0]  # 公司平均底薪
    sql = 'SELECT deptno FROM t_emp GROUP BY deptno HAVING AVG(sal) >= %s'
    # 聚合函數如AVG(), 不能直接寫入WHERE語句, 需要HAVING語法
    cursor.execute(sql,(avg,))
    '''
    for one in cursor:
        print(one[0])  # print(one) -> (20,) (10,)
    '''
    temp = cursor.fetchall()
    print(temp)
    sql = "INSERT INTO t_emp_new SELECT * FROM t_emp WHERE deptno IN ("  # 此時不能用靜態暫未符, 如%s, 因為不確定數量, 所以用拼接語法
    # 如何動態獲取數量, 使用索引
    for index in range(len(temp)):
        data = temp[index][0]  # 取出純數字數據, 並且為逐一執行
        if index < len(temp) - 1:
            # len(temp) - 1 為目前最後一位的索引序號
            sql+= str(data)+','  # 還需轉為字符串型態。判斷當前索引序號是否為最後一個序號, 若否, 加"逗號"在其後
        else:
            sql+=str(data)
    sql+=")"
    print(sql)  # 查看拼接狀態
    cursor.execute(sql)

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
    sql = 'SELECT deptno FROM t_dept WHERE dname=%s'
    cursor.execute(sql, ("SALES",))
    deptno = cursor.fetchone()[0]
    sql = 'UPDATE t_emp_new SET deptno=%s'
    print(sql)
    cursor.execute(sql, [deptno])
    con.commit()
except Exception as e:
   if 'con' in dir():
       con.rollback()
   print(e)