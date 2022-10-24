# coding:utf-8

'''
编写一个小程序，模拟实现双色球开奖，摇出6个红色球号码和1个蓝色球号码，每个号码都是双数，例如9记为09，范围如下
09 29 06 17 08 13   02
红球：从1号到33号共33个数字
篮球：从1号到16号共16个数字
'''

import random

def lucky_draw():
    print('本期双色球中奖号码：\n')
    for i in range(1, 6):
        red = random.randrange(1, 34, 1) # 數字範圍只到33
        if red <= 9:
            red = '0%d' % red
        if i <= 5:
            print(red, end=' ')
        elif i == 6:
            print(red, end='\t')

    blue = random.randint(1, 16) # 1跟16都有包含
    if blue <= 9:
        blue_new = '0%d' % blue
        print(blue_new)
    else:
        print(blue)

if __name__ == '__main__':
    lucky_draw()


