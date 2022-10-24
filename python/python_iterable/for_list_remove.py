# coding: utf-8

list_1 = [3, 6, 8, 9, 25, 36, 100, 105]

for item in list_1:

    if (item % 2 == 0):

        list_1.remove(item)

print(list_1)   # 列表中的8、100仍然存在，偶数元素删除有遗漏。

'''
这是因为remove()删除一个元素之后，后边的元素会自动的覆盖到上一个被删除的元素的位置上，
此时for循环正向运行，正好会略过这个往前移的元素，继续往下走，造成遍历的遗漏。详解如下：
第2次循环，元素6被删除，元素8占据元素6的位置
第3次循环，判断元素9是否为偶数，略过元素8
第5次循环，元素36被删除，元素100占据元素36的位置
第6次循环，判断元素105是否为偶数，略过元素100

'''
# 如何解决呢？
# 逆序删除，从后向前删除，
for item in list_1[::-1]:

   if (item % 2 == 0):

      list_1.remove(item)

print(list_1)
