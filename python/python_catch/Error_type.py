# coding:utf-8

'''
Exception: 通用類 -- 所有異常類的父類
NameError: 沒有這個變量 -- 未初始化對象, 未定義
AttributeError: 對象沒有這個屬性, 方法
ZeroDivisionError: 不能整除0
IOError: 輸入輸出操作失敗 -- 文件讀寫
IndexError: 沒有當前的索引
'''

'''
KeyError: 沒有這個鍵值-Key
SyntaxError: 語法錯誤
SystemError: 解釋器的系統錯誤
ValueError: 傳入的參數錯誤
TypeError: 沒有傳參
'''

class Test(object):
    pass

t = Test()
try:
    t.name
except AttributeError as e:
    print(e)

'''
Traceback (most recent call last):  # 一個錯誤
    # 錯誤文件的絕對路徑; 錯誤的地點; 
  File "C:/Users/user/Desktop/python/python_catch/Error_type.py", line 23, in <module>
    t.name
AttributeError: 'Test' object has no attribute 'name'
# 錯誤類型: Test對象沒有屬性name
'''

d = {'name': '小木'}
try:
    d['age'] # KeyError
except KeyError as e:
    print('沒有對應的鍵:',e)

l = [1, 2, 3]
try:
    l[5]
except IndexError as e:
    print('超出索引: %s' % e)

name = 'dewei'
try:
    int(name)
except ValueError as e:
    print(e)

def test(a):
    return  a

try:
    test()
except TypeError as e:
    print(e)

