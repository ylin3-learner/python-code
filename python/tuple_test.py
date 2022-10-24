# coding: utf-8

tuple_test = ('youlun', )
print(tuple_test)
print(type(tuple_test))
print(bool(tuple_test))

tuple_test1 = (1)
print(type(tuple_test1))

tuple_test2 = ('youlun')
print(type(tuple_test2))

tuple_test3 = ([1, 2, 3])
print(type(tuple_test3))
print(len(tuple_test3))

tuple_final = ([1, 2, 3], )
print(type(tuple_final))
print(len(tuple_final))

tuple_01 = ()
tuple_02 = ('')

print(type(tuple_01))
print(type(tuple_02))
print(bool(tuple_01))
print(bool(tuple_02))
print(len(tuple_02))

a = [1]
b = [2]
c = a + b

print(id(a))
print(id(b))
print(id(c))
print(a, b, c)