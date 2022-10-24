# coding:utf-8

# refer = https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/
import threading, time


def loop():
    n = 0
    while n < 5:
        print('子線程', threading.current_thread())
        print('逆流而上')
        time.sleep(1)
        n += 1

def use_thread():
    print('主線程', threading.current_thread())

t = threading.Thread(target=loop, name='loop_thread')
t.start()
t.join()  # 等待子線程跑完, 主線程才能進行

use_thread()


balance = 0

def change_it(n):
    global balance
    balance += n
    time.sleep(2)
    balance -= n
    time.sleep(1)
    print('n{0}--balance{1}'.format(n, balance))

class Change_thread(threading.Thread):
    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num

    def run(self):
        for i in range(100000):
            change_it(self.num)


t1 = Change_thread(66)
t2 = Change_thread(88)
t1.start()
t2.start()
t1.join()
t2.join()

# 本题考查的是对多线程的创建，Change_thread类继承了threading.Thread类，
# 创建两个线程即创建两个Change_thread类的实例，所以A选项正确。

# 进程是一个执行中的程序并非单独的APP应用


