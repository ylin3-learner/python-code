# coding:utf-8

from redis_demo_2.redis_db import pool
import redis
import time

con = redis.Redis(
    connection_pool=pool
)

con.set("country", "Taiwan")
con.set("city", '雲林')
# city = con.get('city').decode('utf-8')
con.expire('city', 5)
time.sleep(6)
city = con.get('city').decode('utf-8')
print(city)

del con