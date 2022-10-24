# coding:utf-8

from db.mongo_db import client
from bson.objectid import ObjectId

class MongoNewsDao:
    #　添加新聞正文紀錄
    def insert(self, title, content):
        try:
            client.vega.news.insert_one({'title': title, 'content': content})
        except Exception as e:
            print(e)

    # 根據新聞標題, 查找新聞主鍵值
    def search_id(self, title):
        try:
            news = client.vega.news.find_one({'title': title})
            return str(news['_id'])
        except Exception as e:
            print(e)

    # 根據id, 找content_id -> 改title, content
    def update(self, id, title, content):
        try:
            client.vega.news.update_one({'_id': ObjectId(id)},
                                        {'$set': {'title': title, 'content': content}})
        except Exception as e:
            print(e)

    #　根據新聞id, 查找新聞正文
    def search_content_by_id(self, id):
        try:
            news = client.vega.news.find_one({'_id': ObjectId(id)})
            return news['content']
        except Exception as e:
            print(e)

    # 根據新聞id, 刪除新聞
    def delete_by_id(self, id):
        try:
            client.vega.news.delete_one({'_id': ObjectId(id)})
        except Exception as e:
            print(e)