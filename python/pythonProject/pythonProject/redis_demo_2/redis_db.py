# coding:utf-8

import redis

try:
    __config = {
        'host': 'localhost',
        'port': 6379,
        'password': 'abc123456',
        'db': 0,
    }

    pool = redis.ConnectionPool(
        host='localhost',
        port=6379,
        password='abc123456',
        db=0,
        max_connections=500  # 此行決定max_memory上限, data_leak if memory=太大 else 太小
    )
except Exception as e:
    print(e)