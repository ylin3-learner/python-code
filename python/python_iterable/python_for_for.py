# coding: utf-8
print('外層循環执行一次内层循环会把元素从0执行 到结束再继续往下执行。')

for i in range(9):
    for j in range(8):
        print('jjjj內層循環:', j)
        print('iiii外層循環:', i)
        print('=======')
    print('--------')