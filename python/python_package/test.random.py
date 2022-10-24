# coding:utf-8

# 抽獎系統
import random

gifts = ['iphone', 'ipad', 'car', 'tv']

def choice_gifts():
    data = random.choice(gifts)  # 隨機返回序列中的一個選項
    print('你得到了%s ' % data)

def choice_gifts_new():
    count = random.randrange(0, 100, 1)
    if 0 <= count <= 50:
        print('你中了一個iphone', count)
    elif 50 < count <= 70:
        print('你中了一個ipad', count)
    elif 70 < count <= 90:
        print('你中了一個tv', count)
    elif count >= 90:
        print('恭喜你, 你中了一輛小汽車', count)

if __name__ == '__main__':
    choice_gifts_new()
