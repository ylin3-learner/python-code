# coding:utf-8

num1 = input('please input number:')
num2 = input('please input number:')
sum1 = num1 + num2
print('total number is %s' % sum1) # result = str(4) + str(5) -> 45, if want to calculate, type have to be int.
print(type(num1), type(num2))
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue  # continue：強制跳出 ❮本次❯ 迴圈，繼續進入下一圈: i == 5, 不執行打印
    print(i, end=',')

a= set([1, 2, 3])
print(a, type(a))
b= set((1, 2, 3))
print(b, type(b))
# c = set(1, 2, 3)  # set()函數可以創建一個無序不重複的元素集，這個函數至多可以傳一個參數
# print(c, type(c))
d = {1, 2, 3}
print(d, type(d))

text = 'Tomorrow'
print(text.find('m', 3))  # 如果find找不到元素, 會返回-1, index則直接報錯

str = 'https://www.imooc.com'
print(str.find('im', 14))  # 如果find找不到元素, 會返回-1, index則直接報錯

print('%f' % 2000) # %f默認六位小數點

