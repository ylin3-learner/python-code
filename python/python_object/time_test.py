#  coding:utf-8

import time

class test1(object):
    def test2(self):
        self.t = time.localtime()
        print(time.strftime('%Y-%m-%d %H:%M:%S', self.t))
    def test3(self):
        print('readable time is %s' % time.asctime(self.t))
    # return test2() # 外圍函數返回內嵌函數—因為所有的業務都在內, 不返回則無法調用
    # asctime() 函数接受时间元组并返回一个可读的形式如"Tue Dec 11 18:07:14 2008"
if __name__ == '__main__':
    tes = test1()
    tes.test2()
    tes.test3()
# test1()
# 函數有一個參數的話 ->在呼叫函數時則須要給參數的值, 否則會報錯

