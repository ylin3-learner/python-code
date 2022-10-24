# coding: utf-8

# 20以内所有偶数的平方

list_1 = []
for i in range(20):
    if i % 2 == 0:
        list_1.append(i ** 2)
print(list_1)

print([i ** 2 for i in range(20) if i % 2 == 0])
'''
print([x ** 2 for x in range(20) if x % 2 == 0])
# 运行结果：[0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
'''

# 元组推导式
t_1 = (x for x in range(10))  # 结果是生成器对象，使用tuple()函数将其转换为元组
print(tuple(t_1))

# 字典推导式
print({x: x**2 for x in range(10)})

# 集合推导式
print({x for x in range(10)})



for i in range(1, 10):
    for j in range(1, i + 1):
        res = ["%s*%s=%s" % (j, i, i * j)]
        text = '\t'.join(res)   # ['1*2=2', '2*2=4']将列表中的元素用\t字符连接生成一个新的字符串。
        result = '\n'.join(text)  # [['1*1=1'], ['1*2=2', '2*2=4']]将列表中的元素用\n字符连接成新的字符串
        print(result, end='\t')
    print('')
print('~' * 30)
print('\n'.join(['\t'.join(["%s*%s=%s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))
print([["%s*%s=%s" % (j, i, i * j) for j in range(1, i+1)]for i in range(1, 10)])
# 每個元素都變成類表型式, 且每列表型式中的元素由','分隔, 元素數量從1~9
'''
for i in range(10):
	for j in range(1, i+1):
		print('{} * {} = {}'.format(i, j, i * j))
	print()

print([['{} * {} = {}'.format(i, j, i * j) for j in range(1, i + 1]for i in range(10)])
>>> [['1*1=1'], ['1*2=2', '2*2=4'], ['1*3=3', '2*3=6', '3*3=9'],...]]
>['1*2=2', '2*2=4'] 
-- res = {} * {} = {}'.format(i, j, i * j)
'\t'.join(res)
>['1*1=1'], ['1*2=2', '2*2=4']
-- '\n'.join(res)
===> '\n'.join('\t'.join([[{} * {} = {}'.format(i, j, i * j)for j in range(i, i+1)]for i in range(10)]))
'''