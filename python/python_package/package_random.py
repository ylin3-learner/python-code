# coding:utf-8

'''
模塊.模塊中函數
random.random() -> 隨機返回0-1之間的浮點數
random.uniform(a, b) -> 產生a-b間的浮點數

random.randint(a, b) -> 產生a-b間的隨機整數
random.choice() -> 從序列中隨機選擇一項, 序列包含串列、元組、字串、清單
random.sample(obj, 數量) -> 隨機返回對象中指定數量的元素, 返回的都是列表
random.randrange(start, end, length) -> 獲取區間內的一個隨機數
random.shuffle(obj) -> 用於將清單中的元素打亂(洗牌)
'''

import random
print(random.choice([1, '', 'python', {'s': 1}]))

print('-------')
# 這兩個的輸出結果相同
print(random.randrange(1, 100, 1))
print(random.choice(range(1, 100)))

print(random.uniform(1, 10))