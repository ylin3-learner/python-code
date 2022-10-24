# coding:utf-8

# 小朋友分糖果
# 有100个糖果，分给5个小朋友，每个小朋友分20个糖果，启动5个线程，来分糖果吧~
#  提示：5个线程可以看做5个小朋友

# child = children[i]
# while seq = True: 無限執行語句

import random
import threading


children = ['a', 'b', 'c', 'd', 'e']
candybar = list(range(1, 101))

def send(child):
   candy_list = []
   if len(candybar) == 0:  # 總糖果數
       print('100顆糖果已分配完!')
       return

   while len(candy_list) < 20:  # 小朋友被分配到的糖果
       candy = random.choice(candybar)
       # candy_list.append(candy)
       # candybar.remove(candy)
       # list.pop([index=-1]) （默认最后一个元素）

       '''
       使用candybar.pop() -- pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
       同candy = random.choice(candybar)
         candy_bar.remove(candy)
       '''
       '''
       使用random.sample(candy, 1)可以随机取出不重复的元素，
       与random.choice(candy)、sugars.remove(candy)实现同样的效果
       '''
       random.sample(candy, 1)
       print(f'{child}有{len(candy_list)}顆糖了')  # 返回告知哪一位小朋友有幾顆糖果了

   print(f'{child}有拿到這些糖果編號{candy_list}了')


if __name__ == '__main__':
    # 每一個小孩都要給一個線程
    for i in range(len(children)):
        t = threading.Thread(target=send, args=(children[i],))
        t.start()


