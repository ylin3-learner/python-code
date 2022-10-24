# coding:utf-8

# import multiprocessing  # 進程的創建模塊, 使函數與主進程互不干擾

'''
類: Process(target函數名,不須括弧, args函數的參數(元組) ) -創建一個進程類, 並實例化進程對象 -> return 進程對象
    start()
    join() -阻塞/等待程序函數, 使主、次進程順序互調
    kill() -殺死進程
    terminate() 和 kill() 两个函数都用于终止进程，两者在 Windows 系统上一样，
    对于 Unix 系统有所区别，两者的通信机制不同
    在 Unix 上，terminate() 使用 SIGTERM 信号，kill() 方法使用 SIGKILL 信号。
    is_alive() -進程是否存活, return bool
'''

import time
import os
import multiprocessing

def work_a():
    for i in range(10):
        print(i, 'a', os.getpid())  # os.getpid()--返回函數自己的進程id,由此看出是否都處在同個進程下
        time.sleep(1)

def work_b():
    for i in range(10):
        print(i, 'b', os.getpid()) # 主進程
        time.sleep(1)

if __name__ == '__main__':  # 主進程
    start = time.time()  # 主進程1 - 在執行work_a, work_b前, 先記錄當前時間戳
    a_p = multiprocessing.Process(target=work_a)  # 主進程中的子進程1
    # a_p.start() # 子進程1執行
    # a_p.join()
    b_p = multiprocessing.Process(target=work_b)  # 子進程2
    # b_p.start()  # 子進程2執行

    for p in (a_p, b_p):  # 多進程執行
        p.start()

    for p in (a_p, b_p):
        p.join()  # 阻塞, 使指定程序先執行完, 再向後走

    for p in (a_p, b_p):
        print(p.is_alive())  # >>> False 代表當前進程已被結束
    print('時間消耗是: ', time.time() - start)  # 主進程2 - 得知運行時間 => 因為是多進程, 所以主進程與子進程互不影響; 所以主進程先執行
    print('parent pid is %s' % os.getpid())  # 主進程3
