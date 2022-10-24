# coding:utf-8

'''
幼儿园举办捡豆子比赛，两个小朋友为一组，将地上的 50 颗豆子捡起来，请运用异步相关的知
识，根据以下任务提示，编程实现两个小朋友捡豆子，并看看谁捡的豆子多

思路一： asyncio 实现异步
思路二：gevent 实现异步
'''

import random
import asyncio

"""
    async 定义异步函数
    await 执行异步
    gather 将异步函数批量执行
    run 执行主异步函数
"""

# 豆子总数
beans = list(range(1, 51))


async def child_a():
    a_beans = []
    while True:
        res = random.choice(beans)
        a_beans.append(res)
        beans.remove(res)
        await asyncio.sleep(random.random())
        if len(beans) == 0:
            break
    return len(a_beans)

async def child_b():
    b_beans = []
    while 1:
        res = random.choice(beans)
        b_beans.append(res)
        beans.remove(res)
        await asyncio.sleep(random.random())
        if not beans:
            break
    # random.sample(序列,k)，從序列中隨機取得指定長度k的片斷。序列包含串列、元組、字串、清單等。
    return len(b_beans)

'''
返回一個包含 14 個項目的列表。
該列表應包含從指定列表中隨機選擇的值，並且選擇“apple”的可能性應該比其他兩個高 10 倍：

import random
mylist = ["apple", "banana", "cherry"]
print(random.choices(mylist, weights = [10, 1, 1], k = 14))
'''

async def main():
    result = await asyncio.gather(child_a(), child_b())
    return result


if __name__ == '__main__':
    result = asyncio.run(main())
    print("a_beans:", result[0])
    print("b_beans:", result[1])
    if result[0] > result[1]:
        print('a小朋友捡到的比较多')
    elif result[0] < result[1]:
        print('b小朋友捡到的比较多')
    else:
        print('两个人捡到的一样多')



