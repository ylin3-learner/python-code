# coding:utf-8

from mongo_db import client
from gridfs import GridFS
from bson import ObjectId

# 只能根據主鍵刪除

db = client.school
gfs = GridFS(db, collection='book')
try:
    gfs.delete(ObjectId('62d6d3a63abf1d6989caa03a'))
except Exception as e:
    print(e)