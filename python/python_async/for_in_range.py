# coding:utf-8

# 可以看到和雖然用普通變量i但是執行代碼不使用i是一樣的效果。
# 在循环中使用return之后会中止循环
for i in range(0, 3):
    print('dddd')

for _ in range(0, 3):
    print('ssss')

'''
[i for i in range(0,5) if i>2] - Python的for迴圈的另一種方式
'''

import time
import multiprocessing

start = time.time()
b = []

def test1():
    a = [i for i in range(1, 5) if i>2]
    print('大佬的迴圈:', a)
    print('test() wasted time:', (time.time()-start))


def test():
    for i in range(5):
        if i > 2:
            b.append(i)
    print('普通for循環:', b)

if __name__ == '__main__':
    start = time.time()
    p = multiprocessing.Process(target=test1)
    p.start()
    p.join()

    test()
    end2 = time.time()
    print('test2() wasted time{}'.format(end2-start))

