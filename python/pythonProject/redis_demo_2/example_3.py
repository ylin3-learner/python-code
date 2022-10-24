# coding:utf-8

from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)

try:  # 保存序列化數據需要列表
    con.delete('dname')
    con.delete('code')
    con.rpush('dname', '技術部', '銷售部', '廣告部')  # key, value1, value2, value3
    con.lpush('code', 'Java', 'PHP', 'HTML', 'Python')  # lpush -> 把最左邊的插到最右邊
    con.rpop('code')
    res = con.lrange('code', 0, -1)
    for i in res:
        print(i.decode('utf-8'))
    # con.lpop('dname')  # element(the leftest) popped by command, will be returned
    con.lrem('dname', 0, '銷售部')
    result = con.lrange('dname', 0, -1)  # lrange -> print all data in list
    for one in result:
        print(one.decode('utf-8'))
except Exception as e:
    print(e)
finally:
    del con
