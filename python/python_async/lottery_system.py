# coding:utf-8

'''
要过年了，很多商家都在举行购物抽奖活动，抽奖规则一般都是以手机号为主，并且一个手机号只能中奖一次。
现在有20人来参加抽奖活动，帮商家开发一个手机号码的抽奖程序，来抽出3个大奖吧
一等奖：手机，价值3999元
二等奖：平板电脑，价值1999元
三等奖：加湿器，价值198元

有20人来参加抽奖活动, 抽出3个大奖
一个手机号只能中奖一次
'''

import json
from types import FunctionType
import random
import threading
from concurrent.futures import ThreadPoolExecutor

prizes = [
    'The 1st prize: cellphone',
    'The 2nd prize: Ipad',
    'The 3rd prize: humidifier',

]

lock = threading.Lock()

# class Lottery_system(object):
    # def divide_message(self):
    #     self.message = str(input('請輸入手機號:'))
    #     if not isinstance(self.message, (list, set, FunctionType)):
    #         self.message = json.dumps(self.message)

def choose():
    lock.acquire()
    # 从手机列表中随机选出一个中奖手机，其他手机均未中奖
    phone = random.choice(phones)
    # 在从奖池中随机选取一个奖品，视为该手机抽中的奖品
    prize = random.choice(prizes)

    phones.remove(phone)
    prizes.remove(prize)
    result = []
    # TODO: result中的phone == phone
    result.append((phone, prize))
    print(result)
    lock.release()
    return '恭喜手机尾号为{}的用户，抽到{}'.format(str(phone)[-5:-1], prize)











if __name__ == '__main__':
    # lottery_system = Lottery_system()
    t = ThreadPoolExecutor(3)
    phone_num = int(input('請輸入抽獎的用戶人數:'))
    phones = random.sample(range(886000000000, 886999999999), phone_num)

    result = []
    for i in range(3):
        t_result = t.submit(choose)
        result.append(t_result)

    for res in result:
        print(res.result())






