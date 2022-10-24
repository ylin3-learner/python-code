# coding:utf-8


'''
程序会先执行主进程，
执行到 res.get()时会阻塞主进程去执行子进程，5个子进程会异步执行，
等子进程执行结束后再继续执行主进程，
进程池中有位置的话就会向进程池中添加进程
当子进程执行到time.sleep()时CPU会进行切换，
主进程比子进程执行的快从而会输出第二个for循环的结果，
从而第二组之后是先添加进程，得到之前子进程的结果并输出
'''
'''
前五个子进程执行结束之后继续执行第二个for循环主进程，这个时候的主进程和子进程是一起执行的吗？
不会一起执行的，会根据CPU的调度去执行进程，执行哪个是没有办法确定的。
'''
'''
当上锁之后，无论进程池内有多少进程，由于上锁，每一次也只能有一个进程执行，直到所有进程执行结束
'''
'''
为什么可以先用close再使用join呢，这个顺序是怎么判断的呢？
pool.close()是关闭进程池，使其不在接受新的任务。防止任何更多的任务被提交到池中。 
一旦完成所有任务，工作进程将退出。需要在join之前调用
>>> join是阻塞主进程一直到所有子进程完成后才继续运行主进程，否则子进程一直执行就会报错。
>>> 进程池就相当于一辆大巴车，而close相当于大巴车不准上客，join大巴车上的乘客（子进程）都下车之后，大巴车就停运了。
'''
import os
import time
import multiprocessing


def work(count, lock):  # 將鎖傳入函數中
    lock.acquire()  # 此行代碼下方為大門內部, 因此每次只能有一個進程進行
    print(count, os.getpid())  # os.getpid() -返回函數自己的進程id
    time.sleep(5)  # 阻塞程序
    lock.release()  # 解鎖
    return 'result is %s, pid is %s' % (count, os.getpid())


if __name__ == '__main__':
    pool = multiprocessing.Pool(5)  # 此代表線程池(主進程)中有5個子進程

    manager = multiprocessing.Manager()  # 初始化Manager
    lock = manager.Lock()  # 進程鎖


    results = []
    for i in range(20):
        result = pool.apply_async(func=work, args=(i, lock))
        # Pool.apply_async(func, type(args)==tuple) -任務加入進程池(異步), no return
        # 實例化result對象
        results.append(result)

    for res in results:
        print(res.get())  # res.get()能夠獲取apply_async中的返回值
    # time.sleep(20)
    # 進程池屬於主進程中的主線程代碼, 因為函數需要20次, 但只有5個線程;
    # 因此, 主進程執行完畢先關閉退出, 進程池中的進程也被關閉, 因此程序無法被執行完
    # time.sleep(20) 使主進程阻塞20秒, 給進程池時間完成工作
    # 進程池每次5個, 每次停5秒; 共20個 -> 5 * 4 = 20

    # pool.close()  # 若需要長期運行, 則不須退出進程; 但若只使用一次, 並代表無法在接受新任務, 終結生命
    # pool.join()  # 則須關閉; 並阻塞 -> 保證進程池中的所有任務完成後再退出

    # 觀察函數id發現共用, 這代表進程沒被關閉;  每次都5個一組打印, 由於進程池最多5個
    # 而work函數要執行20次, 所以需要等待
    # 異步: 代表任務順序被打亂, 所以每次id順序都不相同
