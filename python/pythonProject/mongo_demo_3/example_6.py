# coding:utf-8

from mongo_db import client
from gridfs import GridFS

db = client.school
gfs = GridFS(db, collection='book')

file = open("C:/Users/user/Desktop/sql源文件/關係型數據庫.docx", 'rb')
args = {'type': 'docx', 'keyword': 'sql'}
gfs.put(file, filename='關係型數據庫.docx', **args)
file.close()


