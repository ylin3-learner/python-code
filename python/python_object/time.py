# coding:utf-8

import time

# time.time() -- 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
print("time.time(): %f " %  time.time())
print( time.localtime( time.time() ))
print(time.asctime( time.localtime(time.time()) ) )

'''
创建一个clock装饰器，用于计算test()函数的运行时间
test()函数：
'''

import time
# clock裝飾器
def clock(func):
    def clocked(*args, **kwargs):
        # 起始時間
        start = time.time()
        # 程序執行
        func(*args, **kwargs)# 在装饰器内部func就是传进来的test( )函数。
        # 結束時間
        end = time.time()
        print(func.__name__, end - start)
    return clocked # 在外圍函數返回內嵌函數—因為所有的業務都在內, 不返回則無法調用
@clock
def test():
    print('裝飾器')
    time.sleep(5)
test() # 在最後呼叫函數即可跑函數裡面的程式碼
# time.strftime('%Y-%m-%d %H:%M:%S', time.(end - start))
'''


在调用test()时，会先执行装饰器clock(func)；
可以将test函数的参数传给了clock( )函数内部的clocked( )函数(注：在这里test函数没有参数)，func即test函数，
在clocked( )函数中应调用func(*args,**kwargs)
'''

