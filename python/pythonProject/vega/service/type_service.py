# coding:utf-8

from db.type_dao import TypeDao

class TypeService:
    __type_dao = TypeDao()  # 創建類的對線 -> 私有變量

    def search_all_type(self):
        res = self.__type_dao.search_all_type()
        return res