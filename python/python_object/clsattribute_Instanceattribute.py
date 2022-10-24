# coding: utf-8

class Boy(object):
    age = 18 # class attribute: 18

if __name__ == '__main__':
    b = Boy() # 實例化對象self
    b.age = 20 # 實例屬性

    print('通過實例屬性來修改後的值')
    print(b.age) # 實例屬性
    print(Boy.age) # class attribute

    print('通過類屬性來修改後的值')
    Boy.age = 25
    print(Boy.age) # class attribute
    print(b.age)  # 實例屬性
