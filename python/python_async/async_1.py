# coding:utf-8

'''
異步： 不會因為前方程序阻塞而影響後方程序的執行, 不阻塞
      輕量級的線程 - 協程
      可以獲取異步函數的返回值, 需要在主進程異步的情況下使用 -> 更適合文件的讀寫
多進程、多線程： 業務方向的處理

異步的庫：

自帶： 關鍵字 -需要先定義異步, 才可使用異步
async 定義異步
      async def test():
        return 'a'
await 執行異步函數
      async def work():
        result = await test()
asyncio 調用async函數
    gather(asyncfunc...) -將異步函數批量執行, return list(函數的返回結果)
    run([task]) -執行主異步函數, 執行函數的返回結果

    async def main():
        result = await asyncio.gather(  # 使用result獲取兩個函數的返回值
            a(),
            b()
        )
        print(result)
    if __name__ == '__main__':
        asyncio.run(main())

第三方庫：gevent -- pip install gevent

Window sys rely on Micosoft Visual C++
Linux sys rely on -pip install wheel
創建協程對象: spawn(Func, args) -返回協程對象
批量處理協程對象: joinall([spawnobj]), return [spawnobj]
'''

# 对异步的理解 - 异步最重要的目的就是实现多任务同时运行
# 为了同步异步的任务，要采用同步信号，手动调整任务的同步机制
# 进程、线程、函数/方法等任务都可以做一个异步编程
'''
虽然异步可以提高效率，但异步间的协调是很复杂的操作，这些操作也需要消耗系统性能
-> 异步编程大大提高了程序的运行效率，因此只要可以用异步方式实现的内容就采用异步编程的方式。
'''

import time
import random
import asyncio
import os
import gevent


def gevent_a():
    for i in range(10):
        print(i, 'a gevent', os.getpid())
        gevent.sleep(random.random() * 2)   # 不一定需要阻塞
    return 'gevent a result'

def gevent_b():
    for i in range(10):
        print(i, 'b gevent', os.getpid())
        gevent.sleep(random.random() * 2)  # 此為業務級別的阻塞
    return 'gevent b result'

async def a():
    for i in range(10):
        print(i, 'a', os.getpid())
        await asyncio.sleep(random.random() * 2)  # random.random()將會返回0-1之間的隨機數字 -> 這表示每一次循環等待的時間都不一樣

    return 'a function'
    # return放在了for里面了，所以只走了一次就返回了

async def b():
    for i in range(10):
        print(i, 'b', os.getpid())  # 顯示在同一個進程下執行 --異步為一種類似線程的存在
        await asyncio.sleep(random.random() * 2)  # time.sleep是 CPU級別的阻塞, 如果CPU被阻塞, 無法達到異步、同步

    return 'b function'

async def main():  # 需要在主進程異步的情況下使用
    result = await asyncio.gather(
        a(),
        b()
    )
    print(result[0], result[1])


if __name__ == '__main__':
    start = time.time()
    # asyncio.run(main())
    g_a = gevent.spawn(gevent_a)
    g_b = gevent.spawn(gevent_b)
    gevent_list = [g_a, g_b]
    res = gevent.joinall(gevent_list)
    print(dir(res[0]))
    print(res[0].value, res[1].value)  # gevent.value 獲取返回值
    print('time is', time.time() - start, os.getpid())
