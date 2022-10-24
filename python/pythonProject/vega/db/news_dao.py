# coding:utf-8

from db.mysql_db import pool

# 查詢新聞表, 新聞類型表, 用戶表

class NewsDao():
    # 查詢待審核新聞列表
    def search_unreviewd_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'SELECT n.id, n.title, t.type, u.username ' \
            'FROM t_news n JOIN t_type t ON n.type_id=t.id ' \
            'JOIN t_user u ON n.editor_id=u.id ' \
            'WHERE n.state=%s ' \
            'ORDER BY n.id DESC ' \
            'LIMIT %s, %s'
            # n.create_time
            cursor.execute(sql, ('待審核', (page-1)*10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查詢待審核新聞列表頁數
    def search_unreviewed_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'SELECT CEIL(COUNT(*)/10) FROM t_news WHERE state=%s'  # 舉例: 如果有21條紀錄, 則顯示3頁, CEIL強制進位
            cursor.execute(sql, ('待審核',))
            count_page = cursor.fetchone()[0]  # 因為結果集只有一條紀錄, 只有一個字段
            return count_page
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 審核新聞 -> 將'待審核' 字段 改為 '已審核'
    def update_unreviewed_news(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'UPDATE t_news SET state=%s WHERE id=%s'
            cursor.execute(sql, ('已審核', id))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查詢新聞列表
    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'SELECT n.id, n.title, t.type, u.username ' \
            'FROM t_news n JOIN t_type t ON n.type_id=t.id ' \
            'JOIN t_user u ON n.editor_id=u.id ' \
            'ORDER BY n.id DESC ' \
            'LIMIT %s, %s'
            # n.create_time
            cursor.execute(sql, ((page-1)*10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查詢新聞總頁數
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'SELECT CEIL(COUNT(*)/10) FROM t_news'  # 舉例: 如果有21條紀錄, 則顯示3頁, CEIL強制進位
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]  # 因為結果集只有一條紀錄, 只有一個字段
            return count_page
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 刪除新聞
    def delete_by_id(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'DELETE FROM t_news WHERE id=%s'
            cursor.execute(sql,[id])
            con.commit()
        except Exception as e:
            print(e)
            if 'con' in dir():
                con.rollback()
        finally:
            if 'con' in dir():
                con.close()

    # 添加新聞
    def insert(self, title, ediotr_id, type_id, content_id, is_top):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'INSERT INTO t_news(title, editor_id, type_id, content_id, is_top, state) '\
                  'VALUES (%s, %s, %s, %s, %s, %s)'
            cursor.execute(sql,(title, ediotr_id, type_id, content_id, is_top, "待審核"))
            con.commit()
        except Exception as e:
            print(e)
            if 'con' in dir():
                con.rollback()
        finally:
            if 'con' in dir():
                con.close()
    # 查找用戶緩存的紀錄
    # 通過新聞id, 查找新聞內文, 標題, 作者,類型
    def search_cache(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'SELECT n.title, n.content_id, t.type, u.username, ' \
                  'n.is_top, n.create_time ' \
                  'FROM t_news n ' \
                  'JOIN t_type t ON t.id=n.type_id ' \
                  'JOIN t_user u ON n.editor_id = u.id ' \
                  'WHERE n.id=%s'
            cursor.execute(sql, [id])
            res = cursor.fetchone()  # 因為結果集只有一條紀錄, 只有一個字段
            return res
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 根據新聞id,查找新聞
    def search_by_id(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'SELECT n.title, t.type, n.is_top ' \
                  'FROM t_news n ' \
                  'JOIN t_type t ON t.id=n.type_id ' \
                  'WHERE n.id=%s'
            cursor.execute(sql, [id])
            res = cursor.fetchone()  # 因為結果集只有一條紀錄, 只有一個字段
            return res
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 更改新聞
    def update(self, id, title, type_id, content_id, is_top):  # 不須傳入editor_id, 因為editor不會變; update_time亦是, 只需傳入當前時間即可
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'UPDATE t_news SET title=%s, type_id=%s, content_id=%s ,is_top=%s, ' \
                  'state=%s, update_time=NOW() ' \
                  'WHERE id=%s '
            cursor.execute(sql,(title, type_id, content_id, is_top, "待審核", id))
            con.commit()
        except Exception as e:
            print(e)
            if 'con' in dir():
                con.rollback()
        finally:
            if 'con' in dir():
                con.close()

    # 根據新聞id, 查找content_id
    def search_content_id(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'SELECT content_id FROM t_news ' \
                  'WHERE id=%s'
            cursor.execute(sql, (id,))
            content_id = cursor.fetchone()[0]  # 獲得一條紀錄, 而這條紀錄只有一個字段 -> cursor.fetchone()[0]
            return content_id
        except Exception as e:
            print(e)
        finally:
            print(type(content_id))  # content_id -> tuple
            if 'con' in dir():
                con.close()

# 如何提前測試功能? 創建對象

# service = NewsDao()
# res = service.search_unreivew_list(1)
# print(res)
