# coding:utf-8

print(abs(-10)) # -返回數字絕對值

result = all(['1', None, True]) # 判斷列表內容是否全為True
help(result) # 打印對象的用法

python = ['flask', 'django', 'tornado'] # 枚舉函數 -跌代時紀錄索引
for index, item in enumerate(python):
    print(index, item)

food = input('你想吃甚麼呢: ')
print(food)

help(input) # 返回此對象的內置函數, 如.append()


class Test(object):
    a = 1
    b = 2

    def __init__(self):
        self.a = self.a
        self.b = self.b

test = Test()
print(test.a)
result = vars(test)
print(result)

print('------')
print(hasattr(test, 'a')) #  hasattr(obj對象, key屬性) -判斷對象中是否有某種屬性, return bool
print(hasattr(list, 'appends'))

print('------')
setattr(test, 'c', 3) # setattr(obj, key, value) -為實例化對象添加屬性與值, no return
print(test.c)
print(vars(test))

print(getattr(list, 'append')) # <method 'append' of 'list' objects>
print('---------')
print(getattr(list, 'append')) if hasattr(list, 'append') else print('不能存在')

a = ['', None, True, 0]
# any(Iterable) -判斷內容是否有True值, 只要有一個為True, 則返回True, return bool
print(any(a))
print(all(a))
# any-> or
# all-> and
