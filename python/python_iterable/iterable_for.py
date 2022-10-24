# coding: utf-8

l = ['dewei', 'xiaomu', 'xiaoman', 'xiaoming']

for i in l:  # for item in iterable:
    print(i)

print('finish')

for i in 'python':
    print(i)

users = ('dewei', 'xiaomu', 'xiaoman', 'xiaoming')

for name in users:
    if name == 'xiaomu':
        print('hello xiaomu')
    else:
        print('hello {}, welcome to learn python!'.format(name))
    print('-' * 5) # 因為這是for循環最後一行語句, 所以他會先打印這行在進入下一個for loop
print('--- finish ---')

users = {'name': 'dewei', 'age': 33}

for i in users:
    print(i, users[i])
# dict use items() to use for loop:
'''
for key,value in dict.items():    items無參數, (key,value)當前dict中的key, value, 返回偽列表
    print(key, value)
'''
users = {'name': 'dewei', 'age': 33}
items = users.items()
print(items)  # 偽列表 dict_items([('name', 'dewei'), ('age', 33)])

for key, value in users.items():
    print(key, value)

users_list = [
    {'username': 'xiaomu'},
    {'username': 'dewei'}
]

for user in users_list:
    print(user)
    print(user.get('username'))
    print(user.get('age'))

'''
for item in range(start 索引的左邊, stop 索引的右邊, step=1 跳步):
    print(item)
    
    返回一個可迭代的以整型為主的對象
'''
# else 在 for循環中, 只有在for循環正常退出後才執行

l = range(0,6)
print(l, type(l))

for i in l:
    print(i)
else:
    print('for循環結束了')


