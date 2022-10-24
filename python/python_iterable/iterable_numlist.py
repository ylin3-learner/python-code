# coding: utf-8

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 0

for num in range(1, 12, 2):
    if num % 2 == 0:
        a += 1
        print('第{}个偶数{}'.format(a, num))
