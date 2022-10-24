# coding:utf-8

import asyncio
import gevent as gevent

async def a():
    print('我是異步a')

async def b():
    print('我是異步b')

async def handle():
    await b()

async def main():
    await asyncio.gather(a(), handle())  # 將異步代碼加入其中批量執行

def gevent_a():
    print('我是異步代碼A')

def gevent_b():
    print('我是異步代碼B')

if __name__ == '__main__':
    asyncio.run(main())  # 使用run方法執行異步函數
    g_a = gevent.spawn(gevent_a)
    g_b = gevent.spawn(gevent_b)
    gevent_list = [g_a, g_b]
    print(gevent.joinall(gevent_list))

