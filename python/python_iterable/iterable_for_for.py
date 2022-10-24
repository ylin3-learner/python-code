# coding:utf-8

a = [1, 2, 3]
b = [4, 5, 6]

for i in a:
    print(i)
    print('-----')
    for j in b:
        print(i + j)
    print('=====')

print(i) # a loop-- i 循環到3
print(j) # b looop-- j 循環到6
