# coding:utf-8

# 此文件重要性為：操作連接不同的數據庫 -mysql, redis, mongodb; 拆分大訂單為小訂單, 計算送貨距離
# 需引用user_dao的數據

from db.user_dao import UserDao

class UserService:
    __user_dao = UserDao()  # 私有變量 表示此對象僅能在此其中被調用

    # 驗證用戶登錄
    def login(self, username, password):
        result = self.__user_dao.login(username, password)
        return result

    # 查詢用戶身分
    def search_user_role(self, username):
        role = self.__user_dao.search_user_role(username)
        return role

    # 添加用戶
    def insert(self, username, password, email, role_id):
        self.__user_dao.insert(username, password, email, role_id)  # 因為需要role相關操作, 所以需要創建role_dao

    # 查詢用戶頁數 -製造當前頁數, 總頁數
    def search_count_page(self):
        count_page = self.__user_dao.search_count_page()
        return count_page

    # 查詢用戶分頁紀錄
    def search_list(self, page):
        result = self.__user_dao.search_list(page)
        return result

    # 修改用戶信息
    def update(self, id, username, password, email, role_id):
        self.__user_dao.update(id, username, password, email, role_id)

    # 根據id, 刪除用戶紀錄
    def delete_by_id(self, id):
        self.__user_dao.delete_by_id(id)

    # 根據用戶名 查詢 user_id
    def search_user_id(self, username):
        user_id = self.__user_dao.search_user_id(username)
        return user_id