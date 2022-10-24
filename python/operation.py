# coding: utf-8

a = 1
b = 2
c = 3

d = a + b + c
d += c
print(d) # 9

d -= a
print(d) # 8

d *= b # d = d * b
print(d) # 16

# """a /= b
# print(a)

a //= b
print(a)

# 取模運算符: 如果能被整除, 返回0; 不能被整除, 返回餘值

'''c %= 1
print(c) # 0
'''

c %= 2
print(c) # 1

f = 10
f **= 2
print(f) # 100

list_01 = [1, 2, 3]
print(list_01 * 2)
tuple_01 = (1, 2, 3)
print(tuple_01 * 2)

'''dict_01 = {"name": 'youlun'}
print(dict_01 * 2)   unsupported operand type(s) for *: 'dict' and 'int'
'''
gb = 1
b = gb * 1024 * 1024 * 1024
print(b)









