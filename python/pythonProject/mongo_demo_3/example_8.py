# coding:utf-8

from mongo_db import client
from gridfs import GridFS
from bson import ObjectId

db = client.school
gfs = GridFS(db, collection='book')
res = gfs.get(ObjectId('62d6d3a63abf1d6989caa03a'))  # 查詢
file = open('D:/data/sql_new_book', 'wb')
file.write(res.read())
file.close()