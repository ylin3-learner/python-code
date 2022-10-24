# coding:utf-8

from mongo_demo_3.mongo_db import client

client.school.teacher.insert_one({'name': '陳隆'})
client.school.teacher.insert_many([
    {'name': '蕾娜'}, {'name': '辛'}, {'name': '安娜'}, {'name': '雷歐'}
])