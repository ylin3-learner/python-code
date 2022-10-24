# coding:utf-8

for i in range(1, 10): # i: 1~9
    for j in range(1, i + 1): # j: 1~9
        print('{} * {} = {}'.format(i, j, i * j), end= ' ')
    print('---')  # newline print('') ----因為print打印完, 會默認跳到下一行

for i in range(1, 10):
    for j in range(1, i + 1):
        res = ["%s*%s=%s" % (j, i, i * j)]
        text = ['\t'.join(res)]
        result = '\n'.join(text)
        print(result, end='\t')
    print('')

print('~' * 30)
print('\n'.join(['\t'.join(["%s*%s=%s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))
print('~' * 30)

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i}x{j}={i * j:2} ', end='')
    print('---')  # newline print() --因為print打印完, 會默認跳到下一行


print('=' * 30)

i = 0
j = 0

while i < 9:
    i += 1  # 0+1 = 1, 8+1 = 9
    while j < 9:
        j += 1   # 0+1 = 1, 8+1= 9
        print('{} * {} = {}'.format(j, i, i * j), end= ', ')  # 1 * 1 = 1, 2 * 1 = 2,...,9 * 1 = 9
        if i == j:
            j = 0
            print() # newline
            break # 因為希望每次只產生到 1 * 1 = 1, 2 * 1,2 = 2, 4


# 计算1到100以内能被3或者7整除，但不能同时被3和7整除的数的个数，运行结果为39
num = 1
count = 0
# 循环条件
while num < 100:
    if (num % 3 == 0 or num % 7 == 0) and num % 21 != 0:
        count +=1
    # 循环体，设置条件
    # 补全代码
    num = num + 1
print(count)