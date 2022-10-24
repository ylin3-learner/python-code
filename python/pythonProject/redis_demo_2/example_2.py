# coding:utf-8

from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)

try:
    con.delete('country', 'city')
    con.mset({'country': 'Taiwan', 'city': 'Yunlin'})   # PS: dict type
    result = con.mget('country','city')  # tuple type
    for one in result:
        print(one.decode('utf-8'))
except Exception as e:
    print(e)
finally:
    del con