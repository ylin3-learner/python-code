# coding:utf-8

'''
使用filter函数，求0-50以内（包括50）的偶数

[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
'''

def use_filter(data):
    # 使用result接收filter过滤偶数值的功能
    result = filter(lambda x: x%2==0, data)  # x除2的餘數為0
    return result

    # 使用data接收0-50的数值
data = list(range(51))
    # 调用use_filter函数传入data,使用result变量接收
result = use_filter(data)
print(list(result))


# 使用map函数，求元组 (2,4,6,8,10,12)中各个元素的5次方
# pow(x,y) 方法返回 x的y次方的值
# 次方的計算用 ** 或是 math.pow()
def pow_five(data):
    # 计算元素的5次方
    # result = pow(data, 5)
    result = data ** 5
    return result

data = (2,4,6,8,10,12)
    # 调用pow_five函数传入data，使用result接收
result = map(pow_five, data)
print(tuple(result))



# 从functools 中导入reduce函数
from functools import reduce


def use_reduce(x, y):
    # 使用result接收两个数的乘积
    result = x * y
    return result



# 使用data接收一个1-20的数值
data = list(range(1, 21))
# 调用use_reduce函数传入data
result = reduce(use_reduce, data)
print(result)