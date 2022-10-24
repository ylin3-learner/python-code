# coding:utf-8

from db.mysql_db import pool

class RoleDao:

    # 查詢角色列表
    def search_list(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'SELECT id, role FROM t_role'  # 舉例: 如果有21條紀錄, 則顯示3頁, CEIL強制進位
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()
