# coding:utf-8

from mongo_db import client

client.school.teacher.update_many(
    {}, {'$set': {'role': ['86們']}}
)
client.school.teacher.update_one(
    {'name': '蕾娜'}, {'$set': {'sex': '女', 'race': '白系種'}}
)
client.school.teacher.update_one(
    {'name': '蕾娜'}, {'$push': {'role': '總指揮官'} }
)