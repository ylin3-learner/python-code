# coding:utf-8

from redis_demo_2.redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)

try:
    con.hmset('9523', {'name': 'Cat', 'country': 'New York', 'sex': 'male'})
    con.hset('9523', 'city', 'Washington')
    con.hdel('9523', 'sex')
    res = con.hexists('9523', 'name')
    print(res)
    result = con.hgetall('9523')
    for one in result:
        print(one.decode('utf-8'), result[one].decode('utf-8'))  # one -> key ,result[one] -> value
except Exception as e:
    print(e)
finally:
    del con