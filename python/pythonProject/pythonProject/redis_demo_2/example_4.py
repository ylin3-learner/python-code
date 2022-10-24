# coding:utf-8

from redis_demo_2.redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)

try:
    # 集合 -需要列表中的元素不可重複
    con.sadd('empno', 8001, 8002, 8003)
    con.srandmember('empno', 1)
    result = con.smembers('empno')
    for i in result:
        print(i.decode('utf-8'))
    con.sismember('empno', 8004)
    # 有序集合 -value: dict type -帶有排序功能的集合
    con.zadd('ename', {'馬雲': 0, '林佑綸': 10, '吳磊': 2})
    con.zincrby('ename', -10, '吳磊')
    res = con.zrevrange('ename', 0, -1)
    for one in res:
        print(one.decode('utf-8'))
except Exception as e:
    print(e)
finally:
    del con