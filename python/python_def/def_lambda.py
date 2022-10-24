# coding:utf-8

# 定義一個輕量化的函數, 即用即刪除只在一處使用的功能

# 有參數: f = lambda: value 調用f();   無參數: f = lambda x,y: x * y 調用f(3, 4)

f = lambda: print(1)
f()

f1 = lambda x,y: x + y  # 也可x=1, y=2
print(f1(1, 2))


users = [
    {'username': 'dewei'},
    {'username': 'xiaomu'},
    {'username': 'asan'}
]
users.sort(key=lambda x: x['username'])  # asan> dewei> xiaomu
print(users)

# coding:utf-8

'''
使用匿名函数改造下面的程序

def circle_area(r):
    area = 3.14 * r * r
    return area
print(circle_area(10))
'''

circle_area = lambda r: 3.14 * r * r
print(circle_area(10))