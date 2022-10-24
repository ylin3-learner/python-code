# coding:utf-8

# python中子類繼承父類的方法 而使用的關鍵字 -- 子類繼承, 就能使用父類的方法

class Parent(object):
    def __init__(self, p):  # 構造函數會自動執行, 不須再調用__init__
        print('hello i am parent %s' % p )

class Child(Parent):
    def __init__(self, c): # c, p為必傳參數
        print('hello i am child %s' % c)
        super (Child, self).__init__('\'parent\'')
        # 如何在子類構造函數中調用父類構造函數? super(當前的(類名/類對象), 類的實例).想調用的函數名()

if __name__ == '__main__':
    c = Child(c="'child'")
