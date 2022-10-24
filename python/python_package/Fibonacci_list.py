# coding:utf-8

ls = [1, 2] # 先有兩個數後面才能有相加的模型持續相加
#ls列表中已经有两个数，所以循环28次
for i in range(1, 29): # 從ls[1]開始加
    #第三个数等于前两个数相加
    #依次将前两个数相加,添加进列表
    ls.append(ls[i]+ls[i - 1])
print(len(ls),ls)
print(ls[-1]) # index從0開始計算

