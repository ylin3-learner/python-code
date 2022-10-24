# coding:utf-8

from mongo_demo_3.mongo_db import client
from gridfs import GridFS
from bson import ObjectId
import math
import datetime

db = client.school
gfs = GridFS(db, collection='book')  # 創建調用函數的對象

book = gfs.find_one({'filename': '關係型數據庫.docx'})
print(book.filename)
print(book.keyword)
print(book.type)

print('%dM' % (math.ceil(book.length/1024/1024)))  # 文件的體積
print('---------------------')

books = gfs.find({'type': 'docx'})
for one in books:
    uploadDate = one.uploadDate + datetime.timedelta(hours=8)
    uploadDate = uploadDate.strftime('%Y-%m-%d %H:%M:%S')
    print(one._id, one.filename, uploadDate)

print('---------------')

res = gfs.exists(ObjectId('62d6d3a63abf1d6989caa03a'))
# Python 三元運算子 ternary operator 的語法:
# condition_is_true if condition else condition_is_false
print('Congradulations!') if not res == True else print('NoFileError')

