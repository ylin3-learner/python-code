# coding:utf-8

from redis_db import pool
import redis
import random  # 模擬隨機

con = redis.Redis(
    connection_pool=pool
)

try:
    con.delete('ballot')
    con.zadd('ballot', {'馬雲': 0, '碼化藤': 0, '張朝陽': 0, '陸銘': 0, '埃里斯': 0, '甲騰應': 0})
    names = ['馬雲', '碼化藤', '張朝陽', '陸銘', '埃里斯', '甲騰應']
    for one in range(0, 300):
        num = random.randint(0, 5)
        name = names[num]
        res = con.zincrby('ballot', 1, name)  # 該元素+1
    print(type(res), res, end='\n')
    result = con.zrevrange('ballot', 0, -1, withscores=True)  # 列出元素 -> 還需加'WITHSCORES'才會有票數
    print(type(result), result)
        # result -> 列表在外, 元組在內 -> 取出元素值, 元素值的分數
    for i in result:
        print(i[0].decode('utf-8'), int(i[1]))  # int() -> 才能確保票數為int
except Exception as e:
    print(e)
finally:
    del con