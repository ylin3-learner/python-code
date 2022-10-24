# coding:utf-8

# double for-loop
# https://blog.csdn.net/Yjdhtg/article/details/120159845?utm_source=app&app_version=5.2.0
from random import sample
a = [
    ['wxq', 25, 30000, '算法工程師', '北京'],
    ['zzw', 25, 15000, '政府關系管理', '上海'],
    ['yq', 30, 7000, '電工', '杭州']
]

for m in a:
    for n in m:
        print(n, end='\n')
    print(m)
    print()  # 使第一級列表的每個元素之間空一列

for m in range(5):
    for n in range(3):
        print(n, end='\n')
    print(n)
    print()

b = ['稳健', '长寿', '身负重任', '坚持不懈', '憨态可掬', '慢条斯理', '轻吞慢吐', '不紧不慢', '细嚼慢咽', '威风凌凌', '玄衫绿帽', '铁甲先锋', '能屈能伸', '寿高年长', '脚踏实地', '龟年鹤寿']
print(sample(b, 5))