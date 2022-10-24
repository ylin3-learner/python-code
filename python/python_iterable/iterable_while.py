# coding: utf-8

# while滿足條件下會無限循環, 不滿足條件條件後將停止循環, no return
'''
while bool_result:
    do
'''

count = 0 # 每次需相加的元素
total = 0 # 總和

while count <= 100:
    total += count
    count += 1

    if count == 10:
        print('count 已經到10了!')
    elif count == 50:
        print('count 已經到50了!')
    elif count == 99:
        print('count 馬上到100了!')
print(total)

users = ['a', 'b', 'c', 'd']
index = 0
length = len(users)

while index <= length - 1:
    print(users[index])
    index += 1

print('-----')

for i in users:
    print(i)
