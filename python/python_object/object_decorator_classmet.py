# coding:utf-8

# class decorator -- 將類函數可不經實例化而被直接調用

'''
@classmethod      self --為實例化對象
def func(cls,..): cls代替普通類函數中的self, 變為cls代表當前操作的是類
    do
'''
# 普通self中可調用classmethod, 但classmethod中不接受普通self
'''
classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象
'''

'''
staticmethod 返回函数的静态方法。=> '该方法不强制要求传递参数'

--# 静态方法无需实例化  
-- # 也可以实例化后调用
'''

'''
property -- 將類函數的執行免去括弧, 類似於調用屬性(變量)
'''

class test(object): # self == object
    def __init__(self, a):
        self.a = a

    def run(self):
        print('run')
        self.jump() # 這證明可在普通類函數中調用classmethod
        self.sleep()
    @classmethod
    def jump(cls): # cls replace self;  # cls : 表示没用被实例化的类本身
        print('jump')
        # cls.run() # 測試能否在classmethod中調用普通類函數, 由於參數為cls,所以用cls.run()調用
    @staticmethod
    def sleep(): # 但無法在此函數內調用cls, self
        print('i want to sleep!')
# 通過實例化
'''
test.run()--報錯 => 
在實例化過程中, python會提前將self傳入需要self的函數括弧中, 所以我們在執行時並不需要傳參
但我們沒有實例化, 無法提前傳
'''
t = test('')  # __init__() missing 1 required positional argument: 'a' --> 沒有給a對應的值
t.run()
test.jump()
# test.jump() --run() missing 'self' =>證明無法在classmethod中調用普通類函數
print('----')
test.sleep() # 用staticmethod可直接調用類(test)
t.sleep()