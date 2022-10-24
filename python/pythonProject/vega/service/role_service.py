# coding:utf-8

from db.role_dao import RoleDao

class RoleService():
    __role_dao = RoleDao()

    # 查詢角色列表
    def search_list(self):
        result = self.__role_dao.search_list()
        return result
