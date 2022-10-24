# coding:utf-8
try:
    height = str(175.5)
    print("身高: " + height + " cm")
    price = 5.5
    weight = int(input("请输入重量，单位(千克):"))
    total_price = price * weight
    print("总价: {}元".format(total_price))
except EOFError as e:
    print(end="")
