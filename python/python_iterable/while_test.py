# coding: utf-8
'''
count的值为0，Python中的0代表False，不满足条件，所以循环体一次也不执行，控制台上没有任何输出结果。
'''
count = 0
while count:
    print(count)
'''计算从1到1000以内所有奇数的和，并进行
输出，结果为250000
'''
# coding: utf-8

sum1 = 0
num1 = 1

while num1 <= 1000:
    if num1 % 2 != 0:
        sum1 += num1
    num1 += 1
print(sum1)

# coding: utf-8

i = 0
sum = 0
while i <= 100:
    i += 1
    if i % 2 != 0:
        continue
    sum += i

print(sum)






