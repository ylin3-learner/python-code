# coding:utf-8

from mongo_db import client

teachers = client.school.teacher.find({}).skip(0).limit(10)

for one in teachers:
    print(one['_id'], one['name'])

names = client.school.teacher.distinct('name')  # 參數； str
for one in names:
    print(one)

stu_names = client.school.teacher.find().sort([('name', -1)])  # 參數: 列表內元組 ; -1 降序
for one in stu_names:
    print(one, type(one), '\n', one['_id'], one['name'])