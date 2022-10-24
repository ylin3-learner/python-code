# coding:utf-8

import random
import gevent

"""
    spawn 创建协程对象
    joinall 批量处理协程对象
"""

# 豆子总数
beans = list(range(1, 51))


def child_a():
    a_beans = []
    while True:
        a_beans.append(random.sample(beans, 2))
        await gevent.sleep(random.random())
        if not beans:
            break
    return len(a_beans)

def child_b():
    b_beans = []
    while 1:
        b_beans.append(random.sample(beans, 2))
        await gevent.sleep(random.random())
        if len(beans) == 0:
            break
    return len(b_beans)


if __name__ == '__main__':
    g_a = gevent.spawn(child_a)
    g_b = gevent.spawn(child_b)
    result = gevent.joinall([g_a, g_b])
    print("a_beans", result[0].value)
    print("b_beans", result[1].value)
    if result[0].value > result[1].value:
        print('a小朋友捡到的比较多')
    elif result[0].value < result[1].value:
        print('b小朋友捡到的比较多')
    else:
        print('两个人捡到的一样多')


