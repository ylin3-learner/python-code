# coding:utf-8

'''
队列是一种数据存储结构，它的数据存储特点类似于排队
先进入队列的会先出来，后进入队列的后出来
因此它的数据只要通过put()放入，get()取出即可
不需要安排取哪些数据进程的数据可放入队列，哪些进程需要
从队列中通过取出，即可使用。
'''
# 使用的模块： queue
# 创建的方法： queue. Queue(…)

import multiprocessing, time, random

def sender(q):
    while True:
        x = random.randint(1, 10)
        print('send done:', x)
        q.put(x)  # 將數據放到了隊列
        time.sleep(1)
        break


def recvder(q):
    while True:
        x = q.get()  # 從隊列中取出數據
        print('recv done:', x * 3.14)
        time.sleep(1)
        break

if __name__ == '__main__':
    q = multiprocessing.Queue()
    t1 = multiprocessing.Process(target=sender, args=(q,))  # args = tuple
    t2 = multiprocessing.Process(target=recvder, args=(q,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

'''
send done: 3
recv done: 9.42
send done: 3
recv done: 9.42
這個程式將造成內存溢出, 但由結果可得知只要放入隊列, 其他函數即可調用
'''