# coding:utf-8

# __str__: when print 實例化對象, 會返回該函數的return信息
'''
def __str__(self):
    return str_type
'''
'''
class Test_str(object):
    def __str__(self): # __name__ 為類的內置函數
        return '這是關於這個類的信息'

test = Test_str()
print(test)
'''
# __getattr__: 當調用的屬性或方法不存在, 會返回該方法定義的信息
'''
def __getattr__(self, key): key為調用任意不存在的屬性名, 返回值可以是任意類型也可以不返回
    print(something)    
'''
'''
class Test_getattr(object):
    def __getattr__(self, key):
        print('這個key:{}不存在'.format(key))

test = Test_getattr()
print(test)
'''
# __setattr__: 攔截當前類中不存在的屬性和值
'''
def __setattr__:
    self.__dict__[key] = value  -- key為當前的屬性名, value為當前的參數對應的值; 無返回值
'''
'''
class Test(object):
    def __setattr__(self, key, value):
        if key not in self.__dict__:  # self.__dict__為存在於類中的內置字典
            self.__dict__[key] = value
            
t = Test()
t.name = 'dewei'
print(t.name)

'''
# __call__: 本質是將一個類變成一個函數
'''
def __call__(self. *args, **kwargs):  # 參數: 可傳任意參數;  返回值: 與函數情況相同可有可無
    print('call with start')
'''
'''
class Test(object):
    def __call__(self, **kwargs):
        print('args is {}'.format(args))
        
t = Test()
t(name = 'dewei')  # 用使用函數的方式調用t()
'''

class Test(object):
    def __str__(self):  # 一般__str__會定義一些關於這個類的描述信息
        return 'this is a test class'

    def __getattr__(self, key): # 使我們在書寫時並不會因為Key 不存在而直接報錯
        return f'這個key:{key}並不存在'

    def __setattr__(self, key, value):
            self.__dict__[key] = value # 加入value到self.__dict__字典中
            print(self.__dict__) # 實際上每一個類中都有這樣的內置字典 self.__dict__

    def __call__(self, a):
        print('call func will start')
        print(a)
t = Test()
print(t)  # <__main__.Test object at 0x0000026819807400> -- 主程序.Test類 它是一個對象 at 內存地址

print(t.a)
print(t.b)

t.name = '小木'
print(t.name) # 打印value

t('dewei')


# t.a.b.c 鏈式操作
class Test2(object):
    def __init__(self, attr=''):
        self.__attr = attr
    def __call__(self, name=''):  # 將c變為一個函數
        print('key is {}'.format(self.__attr))
        return name
    def __getattr__(self, key): # 如果附加的屬性, 函數不存在, 返回值可以是任意類型也可以不返回, key為調用任意不存在的屬性名
        if self.__attr: # 如果set.__attr存在
            key = '{}.{}'.format(self.__attr, key)
        else:
            key = key
        print(key)
        return Test2(key) # 通過類函數調用自己的類對象, 通過括弧實例化 -- 一種遞歸
'''
a
a.b
a.b.c
'''
t2 = Test2() # __init__() missing 1 required positional argument: 'attr' -- 沒有給attr初始化值
t2.a.b.c() # 通過()調用函數, 用t2.a.b.c為調用屬性,

name = t2.a.b.c('dewei')
print(name)

result = t2.name.age.sex('ok')
print(result)