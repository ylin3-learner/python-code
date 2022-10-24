# coding:utf-8

from db.mysql_db import pool

class TypeDao:

    # 查詢新聞類型列表
    def search_all_type(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'SELECT id, type FROM t_type ORDER BY id'
            cursor.execute(sql)
            res = cursor.fetchall()
            return res
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()
