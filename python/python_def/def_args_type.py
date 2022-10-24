# coding:utf-8

# 參數定義類型的方法:　參數名＋冒號＋類型函數　－－name:str, age:int=33

def add(a:int, b:int=3):
     print(a+b)

add(1)
add('hello', 'xiaomu')


def test(a:int, b:int=3, *args:int, **kwargs:str):
    print(a, b, args, kwargs)

test(1, 2, 3, '4', name='xiaomu')  #'4'與類型int不符依然可以打印, 不會判斷驗證和報錯

def test2(a:int, b, c=3):
    print(a, b, c)

test2(1, 3, 4)  # type: 'str, list, tuple, dict, float...'





