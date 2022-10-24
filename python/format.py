# coding: utf-8

info = 'my name is %s, my age is %s'

name_1 = 'xiaomu'
age_1 = 10

name_2 = 'youlun'
age_2 = 19

print(info % (name_1, age_1))
print(info % (name_2, age_2))

message = '你好! 今天是%s, 您的手機號碼是: %s, 已經欠費了, 請盡快繳納!! '
print(message % ('星期五', 123456789))

print(message % (1234567, 'Friday'))
print(message)

books =['Python', 'Django', 'Flask']
info_2 ='my name is %s, my age is %s, my book is %s'
print(info_2 % (name_1, age_2, books))

dict_01 = {'a': 'a', 'b': 'b', 'c': 'c'}
print('dict is %s' % dict_01)

info_3 = 'my name is {}, my age is {}, my book is {}'
print(info_3.format(name_2, age_1, books))

info_4 = f'my name is {name_1}, my age is {age_1}, my book is {books}'
print(info_4)

print(info_3.format('youlun', 33, ['python']))
