# coding:utf-8

import redis
from redis_demo_2.redis_db import pool
import random
from concurrent.futures import ThreadPoolExecutor

# 創建原始用戶id -隨機生成數字充當1000位用戶
s = set()  #　從中獲取並加入 事務中 -> 代表該用戶成功搶到秒殺品

while True:
    if len(s) == 1000:
        break
    else:
        num = random.randint(10000, 100000)
        s.add(num)

# 創建連接
con = redis.Redis(
    connection_pool=pool
)

try:
    con.delete('kill_total', 'kill_num', 'kill_user', 'kill_flag')  # 避免重複執行, 重複插入
    con.set('kill_total', 50)  #　總共50份
    con.set('kill_num', 0)  # 搶到份額
    con.set('kill_flag', 1)  # 過期標誌
    con.expire('kill_flag', 600)  # 時間:秒
except Exception as e:
    print(e)
finally:
    del con

# 導入線程池
executor = ThreadPoolExecutor(200)

def buy():
    try:  # 需要觀看kill_num, kill_user數據變化 -pipeline.watch()
        connection = redis.Redis(
            connection_pool=pool
        )
        pipeline = connection.pipeline()
        pipeline.watch('kill_num', 'kill_user')
        # 須為有效搶購  -標誌位值不重要, 只需判斷存不存在 -> 搭配expire()為實現
        if connection.exists('kill_flag'):
            # 比較目前搶購 與 搶購名額
            total = int(pipeline.get('kill_total').decode('utf-8'))
            num = int(pipeline.get('kill_num').decode('utf-8'))
            if num < total:  # 還可以參與秒殺 -> 秒殺 -開啟事務機制, 以保證此事務不會被打斷, 避免超買, 超賣
                #　kill_num+1, append kill_user_id
                pipeline.multi()
                # 若是可以被其他事務打斷, 將來執行時很可能 +1, ...+inf, 因為速度快到判斷kill_num時, 仍是49
                pipeline.incr('kill_num', 1)
                user_id = s.pop()  # 返回被取出的值, 模擬搶購
                pipeline.rpush('kill_user', user_id)
                pipeline.execute()
    except Exception as e:
        if 'pipeline' in dir():
            pipeline.reset()  # 回收機制 -> 回收連接
        print(e)
    finally:
        del connection

for i in range(0, 1000):
    executor.submit(buy)

print('秒殺已結束')

# 報錯: too many connections
# 因为redis_db中的pool在建立时有一个参数max_connections，这个参数是最大连接数。
# 若参数的值设置的过小，就会提示too many connections，需要改大一些，例如200
