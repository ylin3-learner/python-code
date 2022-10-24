# coding:utf-8

# in-place construction
arr1 = [i for i in range(10)]

# you can use if to filter the elements - 這樣的寫法就等於告訴Python，要在for迴圈內包一層if的意思。
arr2 = [x for x in arr1 if x % 2 == 0]

# you can use as many conditions as you want!
arr3 = [x for x in arr1 if x >= 3 and x % 2]

# use nested for loops to make everyone dizzy - 想像成第一層for迴圈裡面又包了一個for迴圈
arr4 = [(x, y) for x in range(3) for y in range(4)]

print(arr1)
print(arr2)
print(arr3)
print(arr4)

arr5 = (i for i in range(10))
print(type(arr5))
arr_old = list(arr5)
arr_new = list(arr5)
arr_mid = [arr5]
print(arr_old)
print(arr_new)
print(arr_mid)

'''
arr2是空List，原因是generator這個東西被arr1消耗掉了，所以arr2並沒有拿到元素!
'''

'''
請創造兩個陣列
第一個陣列包含1~20中的偶數
另一個包含1~20中的奇數
'''

# arr1 = [i for i in range(1, 21) if i % 2 == 1]
# arr2 = [i for i in range(1, 21) if i % 2 == 0]
#
# for index in range(len(arr1)):
#     print(arr1[index], '<--->', arr2[index])

# 基本上就是分別找出1~20的基數與偶數，用for迴圈取出來，並印出。
# 一開始我們講過如果要在一行輸出多個值，可以將他們通通傳給print函式，他會用空白將他們隔開再一並輸出。

# 今天如果要在一個for迴圈，操作兩個等長的陣列時

arr1 = [i for i in range(1, 21, 2)]
arr2 = [i for i in range(2, 21, 2)]

for t in zip(arr1, arr2):
    print(t[0], t[1], sep=' <---> ')
    # zip這個函式，這個函式會接受不限個數的序列容器，並把他們合而為一，成為一個超大的序列容器
    # 他會把兩個陣列的第一個元素取出，合併為一個tuple，並放進新的序列容器之中。然後第二個...第三個...以此類推。
    # 你可能會好奇，如果給zip的序列容器不等長，結果會怎麼樣?
    # 結果會是以最短的輸入容器為主，做出與之等長的新容器。

"""
現在我們要從一個裝有tuple的容器取出元素，那我們應該怎麼接?
第一種方法，直接用一個變數接住tuple，再用index取值。
第二種方法，既然事先知道壓縮了幾個容器，也就知道裡面tuple的長度，因此用一樣多的變數接住他 (以上面例子來說，要用兩個變數i, j。)
"""

# 輸出值的時候，中間不一定要用空白隔開，你可以給print函式sep這個參數，如此一來就可以用自己喜歡的方式隔開輸出值了!
