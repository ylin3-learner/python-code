# coding:utf-8

# 只要在class內, self就是當前類中屬性與函數的橋樑

'''
面向對向編程:
利用對象的屬性與方法進行編程
Type = class類  類變量(屬性), 類函數(方法)
class Name(object):
	attr =something  類屬性
	def func(self): 類函數
		do
類的名稱首字母大寫, 多單詞情況下每個單詞首字母大寫—駝峰命名

class Person(Object):
	name = ‘xiaomu’
	def dump(self):  # self為必傳參數, 必須為首位; 且self是一個對象, 代表實例化的變量自身
		print(f’{self.name} is dumping!’) # self直接通過點來定義類變量
xiaomu = Person()  類的實例化過程, xiaomu則為person()的實例化對象
print(xiaomu.name)  屬性調用
xiaomu.dump()	函數調用

str, List, dict, tuple -- class
非函數中定義的變量在定義的時候不用self

類的構造函數 – 類的默認函數, 將類實例化的同時,順便傳參 PS: 構造函數定義在最上層
def _init_(self, a, b):  # a, b為希望在方法中傳入的參數
	self.a = a # 類實例的屬性, 就可以在類的各個方法中調用
	self.b = b
Class Test(object):;
	def _init_(self, a):
		self.a = a
	def run(self):
		print(self.a)
t = Test(1) # 因為self為第一個參數為(0),  a 為第二個參數(1)
t.run()
>> 1

'''

'''
Python中为何要有__init__
我的理解是，__init__的出现，主要有两方面的作用：

一般常见的初始化，我的理解，可能主要有两方面：

支持带参数的类的初始化
这个用法，感觉就像，其他语言中的，对于Class初始化时，可以运行传递不同的参数一样
实现类本身相关内容的初始化
当一个Class，稍微复杂一点的时候，或者内部函数需要用得到的时候，
往往都需要在，别人实例化你这个类之前，使用你这个类之前，做一些基本的，与自己的类有关的，初始化方面的工作。

而这部分工作，往往就放到__init__函数中去了。

换句话说，你要用人家的类（中的变量和函数）之前，总要给人家一个机会，做点准备工作，然后才能为你服务吧。
'''
class Person(object):

    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name}在奔跑')

    def jump(self):
        print(f'{self.name}在跳躍')

    def work(self):
        self.run()
        self.jump()
        def sleep(name):
            return name
        result = sleep(self.name)
        print('sleep result is %s' % result)

xiaomu = Person(name='小慕', age=10) # 實例化類
xiaomu.name = 'xiaomu'# 屬性賦值修改只針對當前的實例化對象, 類不會有影響
xiaomu.jump()# 調用實例化中的方法

dewei = Person(name='dewei')
dewei.jump()

dewei.top = 174
print(dewei.top) # 實例化對象可以自定義屬性
print(dewei.age)
print('------')
xiaomu.work()
