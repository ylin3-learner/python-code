# coding:utf-8
sales = {
'weipinhui': 8872131,
'jingdong': 51073400,
'xiaomu': 460500,
'suning': 15843900,
'dangdang': 1000000,
'guomei': 4500000,
'tianmao': 1200000
}
sales_num = list(sales.values())
sales_num.sort()
print(sales_num)

for key,value in sales.items():
    if value == sales_num[0]:
        print('Min:', key, value)
    if value == sales_num[len(sales_num)-1]:
        print('Max:', key, value)


# coding: utf-8
# Solution 2 of 電商銷售額比較
# coding:utf-8
dict = {
        '唯品会': 8872131,
        '京东': 51073400,
        '小米科技': 4605000,
        '苏宁易购': 15843900,
        '当当网': 1000000,
        '国美零售': 4500000,
        '天猫自营': 1200000}
for key, value in dict.items():
    if value == max(dict.values()):
        print('Max: ', (key, value))
    if value == min(dict.values()):
         print('Min: ', (key, value))








