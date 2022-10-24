# coding:utf-8

'''
1、在每个奖品只有一个情况下，为避免多个手机号同时抽中同一个奖需要加锁，保证只有一个手机号在抽奖；
2、每个手机号只能抽奖一次可以理解为：生成20个不同的同手机号，放进一个列表中，随机使用手机号抽奖并从列表中删除手机号，保证每个手机号只能抽一次。
'''

import threading
import random
from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()
def luck_draw(arg):
    lock.acquire()
    # 从手机列表中随机选出一个中奖手机，其他手机均未中奖
    phone = random.choice(arg[0])
    # 在从奖池中随机选取一个奖品，视为该手机抽中的奖品
    price = random.choice(arg[1])
    prices.remove(price)
    phones.remove(phone)
    lock.release()
    return '恭喜手机尾号为{}的用户，抽到{}'.format(str(phone)[-5:-1], price)

if __name__ == '__main__':
    t = ThreadPoolExecutor(3)       # 通过创建三个线程从而实现每个线程完成一项抽奖任务
    # 确定抽奖人数
    phone_num = int(input('请输入抽奖的用户人数：'))
    # 模拟产生出相应数量的手机号
    phones = random.sample(range(17800000000, 17899999999), phone_num)
    prices = ['一等奖：iPhone12 ProMax', '二等奖：ipad2021pro', '三等奖：air wetter']
    result = []
    for i in range(3): # 三个任务，每个线程分配一个
        t_result = t.submit(luck_draw, (phones, prices))
        result.append(t_result)

    for res in result:
        print(res.result())

