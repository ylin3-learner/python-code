# coding:utf-8

from db.redis_db import pool
import redis

class RedisNewsDao:

    def insert(self, id, title, username, type, content, is_top, create_time):
        con = redis.Redis(
            connection_pool=pool
        )
        try:
            con.hmset(id, {
                'title': title,
                'author': username,
                'content': content,
                'type': type,
                'is_top': is_top,
                'create_time': create_time
            })
            # 如果is_top==0, 不去置頂新聞, 過期時間24小時
            if is_top == 0:
                con.expire(id, 24*60*60)  # 秒
        except Exception as e:
            print(e)
        finally:
            del con

    # 刪除緩存的新聞
    def delete_cache(self, id):
        con = redis.Redis(
            connection_pool=pool
        )
        try:
            con.delete(id)  # 若無資料也不會報資料 返回空str
        except Exception as e:
            print(e)
        finally:
            del con