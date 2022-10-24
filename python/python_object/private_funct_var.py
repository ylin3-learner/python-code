# coding:utf-8

'''
class Person(object):
    def _init_(self, name):
        self.name = name
        self.__age = 33  # private funct,
    def dump(self):
        print(self.name, self__age)
    def __cry(self):
        return 'I want to cry'
'''

class Cat(object):  # 1 class, two public funct, two private funct
    _cat_type = 'cat' # 私有屬性
    def __init__(self, name, sex):
        self.name = name
        self.__sex = sex  # 透過私有變量定義sex=sex
    def run(self):
        result = self.__run()  # 定義局部變量result
        print(result)

    def __run(self): # 私有函數
        return f'{self._cat_type}小貓{self.name} {self.__sex}開心的奔跑著!'

    def jump(self):
        result = self.__jump()
        print(result)

    def __jump(self): # 私有函數
        return f'{self._cat_type}小貓{self.name}{self.__sex}開心地跳著'


def test(object):
    pass # 一個占位符, 在還沒確定具體業務前先占位, 否則將會報錯


cat = Cat(name='米粒兒', sex='boy') # 實例化類
cat.run()  # 調用內置函數run()
cat.jump()  # 調用內置函數jump()
# cat.__run() # 私有函數不能用實例化對象調用
print(dir(cat))
print(cat._Cat__jump())  # 雖然可以, 但既然定義為私有函數, 就是不希望實例化對象可以調用
#print(cat.__sex)
# 分別創建兩個私有變量-- 一個透過屬性, 一個透過構造函數添加
