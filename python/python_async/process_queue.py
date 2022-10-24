# coding:utf-8

import multiprocessing
import json
import time
from types import FunctionType  # types類, FunctionType函數

class Work(object):
    def __init__(self, q):
        self.q = q

    def send(self, message):
        if not isinstance(message, (str, set, type, FunctionType)):  # messsage不是str, set, list, Functiontype
            message = json.dumps(message)  # json.dumps() -反序列化 json.dumps 用于将 Python 对象编码成 JSON 字符串。
        self.q.put(message)  # 隊列

    def send_all(self):
        for i in range(20):
            self.q.put(i)
            time.sleep(1)

    def receive(self):
        while 1: # 同while True:
            result = self.q.get()  # 獲取到一條信息
            try:  # 判斷是否是json對象, 有可能不是json字符串
                res = json.loads(result)  # 如果符合json類型, 返回原本數據類型
            except:  # 並不需要捕獲所有異常
                res = result  # 如果不符合, 代表只是普通的字符串
                # 即使出现异常也是要得到从队列中get到的数据的，因此直接将result的值赋值给了res
            print('recv is %s' % result)


if __name__ == '__main__':
    q = multiprocessing.Queue()
    work = Work(q)
    # 上方2行為主進程
    send = multiprocessing.Process(target=work.send, args=({'name': '小慕'},))  # 定義send傳入的進程
    recv = multiprocessing.Process(target=work.receive)
    send_all_p = multiprocessing.Process(target=work.send_all)

    send_all_p.start()
    send.start()
    recv.start()

    send_all_p.join()  # 因為時間最長, 所以最需要阻塞主進程等待send_all_p執行完畢
    # send.join() 但若只有這樣, recv不知何時退出, 因為一直while循環
    # 在线程或进程中都需要用到，join是阻塞主线程（进程）
    # 报错是和操作系统有关，MAC电脑默认启动进程的方式是fork，
    # 使用此方式启动的进程，基本等同于主进程(即主进程拥有的资源，该子进程全都有)。
    # 在执行时会触发SemLock锁。send.join()语句使主进程进入阻塞状态，等待send进程执行完，然后再继续执行主进程
    '''
    如果没有使用join阻塞，主进程执行速度过快，主进程执行结束意味着整个程序执行结束，子进程还没开始，整个程序就执行结束了。
    '''

    # 若使用recv.join() -則程序無法退出, 由於while True, join()等不到recv執行完畢, 所以一直阻塞
    # 造成terminate()無法正常執行
    recv.terminate()  # 強行終結接收端, 導致send_all來不及傳輸到20


