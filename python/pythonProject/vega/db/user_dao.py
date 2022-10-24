# coding:utf-8

# 將對數據庫的操作都放入同一個對象

from db.mysql_db import pool # 引用連接池

class UserDao:
    # 驗證用戶登錄
    def login(self, username, password):
        try:  # 因為都是查詢語句, 就不須事務管理
            con = pool.get_connection()
            cursor = con.cursor()
            # 驗證帳密: 搜尋數據庫中有無匹配帳密, 若無, 則登錄失敗
            # 另外, 無須擔心數據量過大, sql必須先匹配username才會進行解密
            sql = 'SELECT COUNT(*) FROM t_user WHERE username=%s'\
            'AND AES_DECRYPT(UNHEX(password), "HelloWorld")=%s'
            cursor.execute(sql, (username, password))
            num = cursor.fetchone()[0]  # 因為不管有幾個匹配帳密, 返回的都是數字而已
            return True if num == 1 else False  # 三元運算符
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():  # 因為需要多次操作, 每一次用完都必須歸還連接讓下一個sql使用
                con.close()

    # 查詢用戶身分 -將user表與role表連接
    def search_user_role(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'SELECT r.role FROM t_user u JOIN t_role r ON u.role_id=r.id WHERE u.username=%s'
            cursor.execute(sql, (username,))
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            # dir() 函数的作用是返回当前范围（当前模块）内的变量、方法和定义的类型列表获得的属性列表。
            if 'con' in dir():
                con.close()

    # 添加用戶
    def insert(self, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = 'INSERT INTO t_user(username, password, email, role_id) '\
            'VALUES(%s, HEX(AES_ENCRYPT(%s, "HelloWorld")), %s, %s)'
            cursor.execute(sql,(username, password, email, role_id))
            con.commit()
        except Exception as e:
            print(e)
            if 'con' in dir():
                con.rollback()
        finally:
            if 'con' in dir():
                con.close()

    # 查詢用戶頁數 -製造當前頁數, 總頁數
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'SELECT CEIL(COUNT(*)/10) FROM t_user'
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            # dir() 函数的作用是返回当前范围（当前模块）内的变量、方法和定义的类型列表获得的属性列表。
            if 'con' in dir():
                con.close()


    # 查詢用戶分頁紀錄
    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'SELECT u.id, u.username, r.role ' \
                  'FROM t_user u JOIN t_role r ' \
                  'ON u.role_id = r.id ' \
                  'ORDER BY u.id ' \
                  'LIMIT %s, %s'
            cursor.execute(sql, ((page-1)*10, 10))  # 起始值, 一頁顯示10條數據
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            # dir() 函数的作用是返回当前范围（当前模块）内的变量、方法和定义的类型列表获得的属性列表。
            if 'con' in dir():
                con.close()

    # 修改用戶信息
    def update(self, id, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            # 用戶密碼加密
            sql = 'UPDATE t_user SET username=%s, ' \
                  'password=HEX(AES_ENCRYPT(%s, "HelloWorld")), ' \
                  'email=%s, role_id=%s ' \
                  'WHERE id=%s'  # 決定用戶身分
            cursor.execute(sql,(username, password, email, role_id, id))
            con.commit()
        except Exception as e:
            print(e)
            if 'con' in dir():
                con.rollback()
        finally:
            if 'con' in dir():
                con.close()

    # 根據id, 刪除用戶紀錄
    def delete_by_id(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            # 用戶密碼加密
            sql = 'DELETE FROM t_user WHERE id=%s'  # 決定用戶身分
            cursor.execute(sql,[id])
            con.commit()
        except Exception as e:
            print(e)
            if 'con' in dir():
                con.rollback()
        finally:
            if 'con' in dir():
                con.close()

    # 根據用戶名 查詢 user_id
    def search_user_id(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = 'SELECT id FROM t_user WHERE username=%s'
            cursor.execute(sql, [username])
            user_id = cursor.fetchone()[0]  # return tuple
            return user_id
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()