# coding:utf-8

# 全局變量: 在腳本上最上層的變量, 可被取出與使用; 但無法修改
# 局部變量: 在函數體內定義的變量; 局部變量無法在自身函數以外使用
# global: 將使全局變量可以在函數內部修改, 只能在本函数内使用,不能被多个函数使用 --global 全局變量; 工作中不建議使用global修改 ==但只支持num,str, None, bool
# 如果想在局部使用列表, 字典; 不須使用global
name = 'dewei'
age = 33
def test():
    print(name)

test()  # 需傳參否則無法打印

def test1():
    name = 'xiaomu'  # 當重名:優先使用局部變量
    print('函數體內:', name)

test1()
print('函數外:', name)

def test3():
    age = 33
    print(age)

test3()


def test4(a):
    a= 10

test4(name)
print(name)

def test5():
    global name
    global age
    name = 10
    age = 44
test5()
print(name)
print(age)


test_dict ={'a': 1, 'b': 2}  # 全局變量

def test6():
    test_dict['c'] = 3   # 如果想在局部使用列表, 字典; 不須使用global
    test_dict.pop('a')

test6()
print(test_dict)


