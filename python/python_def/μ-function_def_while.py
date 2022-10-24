# coding:utf-8

# 遞歸函數: 一個函數反覆不斷的將自己執行 --避免濫用遞歸, 造成內存溢出而死機
'''
def test(a):
    print(a)
    return test(a) --通過返回值, 直接執行自身函數
'''

count = 0

def test():
    global count
    count += 1

    if count != 5:
        print('count條件不滿足, 我要重新執行我自己! 當前count是 %s' % count)
        return test()
    else:
        print(f'count is {count}')

test() # 需傳參否則無法打印


# coding:utf-8

'''
1、在python的布尔类型中1为True，if n == 0 or 1  的意思为：如果n等于0或者为1（True）满足一个条件则进入条件语句，1为True满足条件直接进入条件语句返回1；

2、if n == 0 and 1  的意思为：在n==0和为1(相当于在n==0时)，则进入条件语句，返回1到上一层调用的函数，返回到n * Recursion(n - 1)结束递归；
'''

"""
当执行Recursion(5)时，n的值是5 -- return 5 * [Recursion(4)=return 4 * {Recursion(3)] = return 3 * (Recursion(2)} = return 2*Recursion(1))
Recursion(1) = 1 ==> Recursion(5) = 5*4*3*2*1
"""

def Recursion(n):

    #判断参数n是否为1或0,如果是返回1
    if n == 0 and 1:  # if n == 0 or n == 1
        return 1
    #否则计算并调用本身进行递归，return返回计算结果
    else:
        return n * Recursion(n - 1)
#打印返回值
print(Recursion(5))