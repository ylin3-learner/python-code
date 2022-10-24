# coding:utf-8

from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)

try:
    con.delete('9527')
    pipeline = con.pipeline()
    pipeline.watch('9523')
    pipeline.hset('9523', 'name', 'Tony')
    pipeline.hset('9523', 'age', 20)
    res = pipeline.hgetall('9523')
    for i in res:
        print('{}:{}'.format(i.decode('utf-8'), res[i].decode('utf-8')), end='; ')
    pipeline.execute()
except Exception as e:
    print(e)
finally:
    if 'pipeline' in dir():
        pipeline.reset()
    del con
    i = 1
    for i in range(1):
        print('hello World', end='; ')
    while i < 3:
        print('hello World')
        i += 1