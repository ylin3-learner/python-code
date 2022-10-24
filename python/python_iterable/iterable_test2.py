# -*- coding:utf-8 -*-



# 定义一个整数

n = 8



dict1={}

for i in range (1,n+1):

    dict1.setdefault(i,i**2)

print(dict1)

# -*- coding:utf-8 -*-

# 定义一个整数
n = 8
d = {}
for i in range(1, n + 1):  # range(start, stop, step)--start~stop左含右不含
    d[i] = i * i  # 添加字典{i:i*i}

print(d)