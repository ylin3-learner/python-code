# coding:utf-8

iter_obj = iter((1, 2, 3)) # 創建迭代器

# 第2種創建迭代器方法
iter_obj_2 = (i for i in range(10)) # 將創建一個迭代器對象

for i in iter_obj_2:
    print(i)
print('=======')
for i in iter_obj_2:
    print(i)

def _next(iter_obj):
    # 使程序可以正常結束, 不會拋出異常
    try:  # 第一種調用方法 -next
        return next(iter_obj)
    except StopIteration: # 因為一定知道會報錯, 所以不用起別名
        return None
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj)) Error: StopIteration
'''
print(_next(iter_obj))
print(_next(iter_obj))
print(_next(iter_obj))
print(_next(iter_obj))
當iter對象讀取完成後, 將無法在讀取
'''
# 第2種調用方法 for loop
# for i in iter_obj:
#     print(i) 比用next調用還要友好的多

# 第一種創建迭代器方法
def make_iter():
    for i in range(10):
        yield i  # 取代next(iter_obj)將迭代器中的數據返回

iter_obj = make_iter()  # 將返回一個迭代器對象
# print(type(iter_obj))  # <class 'generator'> -> 迭代器的意思

for i in iter_obj:
    print(i)
print('---------')
for i in iter_obj: # 當調用時, 每次都將放入內存中, 但一旦讀取完畢將被釋放, 才會內存數據為空
    print(i)

