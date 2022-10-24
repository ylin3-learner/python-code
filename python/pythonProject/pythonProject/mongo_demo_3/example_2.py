# coding:utf-8

from mongo_demo_3.mongo_db import client

try:
    teachers = client.school.teacher.find({})
    for one in teachers:
        print(one['_id'], one['name'])
    print('---------------')
    teacher = client.school.teacher.find_one({'name': '蕾娜'})
    print(teacher['_id'], teacher['name'])
except Exception as e:
    print(e)