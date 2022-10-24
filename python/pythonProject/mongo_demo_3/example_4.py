# coding:utf-8

from mongo_db import client

try:
    client.school.teacher.delete_one({'name': '辛'})
    client.school.teacher.delete_many({'name': '86們'})
    print('我們已先走一步了...')
except Exception as e:
    print(e)