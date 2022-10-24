# coding:utf-8

# property -- 將類函數的執行免去括弧, 類似於調用屬性(變量)
'''
@property
def func(self):
    do          -- 參數介紹: 無重要函數說明
'''

class test(object):
    def __init__(self, name):
        self.name = name

    @property
    def call_name(self):
        return 'hello {}'.format(self.name)

Test = test('xiaomu') # xiaomu = self
result = Test.call_name # 用@property -- 不須括弧, 類似私有變量
print(result)

class test1(object):
    def __init__(self, name):
        self.__name = name # __name => 為私有變量

    @property
    def name(self):
        return self.__name

    @name.setter  # @property的參數值修改方式 --用@var.setter(self, new_var), 重新給var賦值為new_var
    def name(self, value):
        self.__name = value


t1 = test1(name='dewei')
print(t1.name)
# t1.name = 'xiaomu' # AttributeError: can't set attribute, 因為@property有不同的參數修改方式
# print(t1.name)
t1.name = 'xiaomu'
print(t1.name)