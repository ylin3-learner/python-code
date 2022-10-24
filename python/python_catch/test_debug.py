# coding:utf-8
'''
Bug:
    mistake in codes, without 異常捕獲, directly raise by code leading a collapse of system
'''
print('test1')
a = 1
print(a)
print('test2')
b = 2
print(b)
print('test3')
c = 3
print(c)
print('test4')
d = 4
print('test5')
def test():
    print(5)

test()