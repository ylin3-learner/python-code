# coding:utf-8

# 看下pymongo的版本，若为4.0及以上，则需要使用下述方法：
# client = MongoClient(host='127.0.0.1', port=27017, username='admin', password='abc123456')
from pymongo import MongoClient

# client = MongoClient(host='localhost', port=27017)
# client.admin.authenticate('admin', 'abc123456')

client = MongoClient(host='127.0.0.1', port=27017, username='admin', password='abc123456')