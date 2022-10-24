# coding:utf-8

from db.news_dao import NewsDao
from db.redis_news_dao import RedisNewsDao
from db.mongo_news_dao import MongoNewsDao

class NewsService():
    __news_dao = NewsDao()
    __redis_news_dao = RedisNewsDao()
    __mongo_news_dao = MongoNewsDao()

    # 查詢待審核新聞列表
    def search_unreviewed_list(self, page):
        result = self.__news_dao.search_unreviewd_list(page)
        return result

    # 查詢待審核新聞列表頁數
    def search_unreviewed_count_page(self):
        count_page = self.__news_dao.search_unreviewed_count_page()
        return count_page

    # 審核新聞 -> 將'待審核' 字段 改為 '已審核'
    def update_unreviewed_news(self, id):
        self.__news_dao.update_unreviewed_news(id)

    # 查詢新聞列表
    def search_list(self, page):
        result = self.__news_dao.search_list(page)
        return result

    # 查詢新聞總頁數
    def search_count_page(self):
        count_page = self.__news_dao.search_count_page()
        return count_page

    # 刪除新聞 -id是mysql的新聞主鍵值, content_id是mongodb的新聞主鍵值
    def delete_by_id(self, id):
        content_id = self.__news_dao.search_content_id(id)
        self.__news_dao.delete_by_id(id)
        self.__mongo_news_dao.delete_by_id(content_id)

    # 添加新聞  -插入mongodb新聞正文, 插入mysql新聞id
    def insert(self, title, ediotr_id, type_id, content, is_top):
        self.__mongo_news_dao.insert(title, content)
        content_id = self.__mongo_news_dao.search_id(title)
        self.__news_dao.insert(title, ediotr_id, type_id, content_id, is_top)

    # 查找用戶緩存的紀錄
    # 通過新聞id, 查找新聞內文, 標題, 作者,類型
    def search_cache(self, id):
        result = self.__news_dao.search_cache(id)
        return result

    # 向redis保存緩存的新聞
    def cache_news(self, id, title, username, type, content, is_top, create_time):
        self.__redis_news_dao.insert(id, title, username, type, content, is_top, create_time)

    # 刪除緩存的新聞
    def delete_cache(self, id):
        self.__redis_news_dao.delete_cache(id)

    # 根據新聞id,查找新聞
    def search_by_id(self, id):
        result = self.__news_dao.search_by_id(id)
        return result

    # 更改新聞  -> 在控制台寫文本地址 -> 讀取文本內容 -> 利用app.py傳參新聞正文, 而非content_id
    def update(self, id, title, type_id, content, is_top):
        content_id = self.__news_dao.search_content_id(id)  # 此為查詢出來的, 而非傳入的
        self.__mongo_news_dao.update(content_id, title, content)  # 根據content_id, 修改mongodb的新聞title, content
        self.__news_dao.update(id, title, type_id, content_id, is_top)  # 更改mysql
        self.delete_cache(id)  # flushdb redis

    # 　根據新聞id, 查找新聞正文
    def search_content_by_id(self, id):
        content = self.__mongo_news_dao.search_content_by_id(id)
        return content