# coding:utf-8

# 自定義拋出異常函數: raise 異常類型(message=錯誤信息)-- 將信息以報錯的信息拋出
'''
raise ValeError('主動拋出異常類型') >> ValueError: '主動拋出異常類型'
'''

def test(number):
    if number == 100:
        raise ValueError('number 不可以是100')
    return number # if number != 100, return number

print(test(50))
# test(100)

# 可以通過try, except監控我們自定義的raise Error(message)
def test2(number):
    try:
        return test(number) # return 調用test函數並順便傳number進去;
        # 由於test()我們使用raise--報錯, 進入到except, return e並打印
    except ValueError as e:
        return e

print(test2(100))


# 能否達成raise (message) -- 不行, 一定要配合異常類型使用

def test3():
    try:
        raise Exception('wrong')
    except Exception as e:
        print(e)
test3()

def test4(name):
    try:
        if name == 'dewei':
            raise Exception('dewei can not be written')
        return name
    except Exception as e:
        print(e)
test4('dewei')


# 自定義異常類型: 參考 raise Exception(message)
'''
1. 繼承基類: Exception
2. 在構造函數中定義錯誤信息
'''

'''
class NewError(Exception): #  繼承基類: Exception
    def __init__(self, message): #  在構造函數中定義錯誤信息
        self.message = message

def test():
    raise NewError('this is a bug') # 調用自定義的異常類

try: # 用try, except捕獲異常信息
    test()
except NewError as e:
    print(e)

test()
'''

class NumberLimitError(Exception):
    def __init__(self, message):
        self.message = message  # 代碼規範: 類與類之間要兩個空行


class NameLimitError(Exception):
    def __init__(self, message):
        self.message = message

def test5(name):
    if name == 'dewei':
        raise NameLimitError('dewei不可以被填寫')
    return name # if name != 'dewei' , return name

def test6(number):
    if number > 100:
        raise NumberLimitError('數字不可以大於100')
    return number # if number <= 100, return number

print('-------')

try:
    test5('dewei')
except NameLimitError as e:
    print(e)

try:
    test6(1000)
except NumberLimitError as e:
    print(e)

test5('dewei')