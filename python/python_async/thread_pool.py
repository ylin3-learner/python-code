# coding:utf-8

import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor

# 線程只需要在全局加鎖, 但進程需要把鎖傳入函數

lock = threading.Lock()  # 全局鎖

def work(i):
    lock.acquire()
    print(i, os.getpid())
    time.sleep(1)  # 因為此函數運行過快, 需要阻塞一下, 模擬長時間運行
    lock.release()
    return 'result %s' % i


if __name__ == '__main__':
    print(os.getpid())  # 主進程id
    t = ThreadPoolExecutor(2)
    result = []
    for i in range(20):
        t_result = t.submit(work, (i, ))  # 同時執行造成結果: (14,)(15,) -> 因此需要加鎖, 使其一次一個
        result.append(t_result)

    for res in result:
        print(res.result())

