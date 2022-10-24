# coding:utf-8

'''
生产者消费者模型当中有两大重要的角色，一个是生产者（负责生产数据的任务），另一个是消费者（接收生产出来的数据，并进行进
一步的操作）
已知慕慕是生产者，为小朋友们制作小蛋糕，共制作了 10 只小蛋糕
小明、小红、安安 3 人是消费者，将慕慕制作的小蛋糕全部吃掉
'''

import threading
import time
import queue
import json
from types import FunctionType

# 创建队列
q = queue.Queue()


# 生产者
def Producer(name):
    if not isinstance(name, (str, set, FunctionType)):
        name = json.dumps(name)
    for i in range(1, 11):
        # 将制作的小蛋糕放入队列中
        q.put(i)
        print(f'{name}做的蛋糕已放入隊列{i}')
        time.sleep(1)


# 消耗者
def Consumer(name):
    while True:
        # 取出蛋糕并吃掉
        cake = q.get()
        try:
            result = json.loads(cake)
        except:
            result = cake
        print(f'{name}已取出蛋糕{cake}並吃掉')





if __name__ == '__main__':
    # 创建线程，一个生产者，三个消费者
    p = threading.Thread(target=Producer, args=('慕慕',))
    c1 = threading.Thread(target=Consumer, args=('小明',))
    c2 = threading.Thread(target=Consumer, args=('小红',))
    c3 = threading.Thread(target=Consumer, args=('安安',))

    p.start()
    time.sleep(3)

    for c in (c1, c2, c3):
        c.setDaemon(True)
        c.start()









