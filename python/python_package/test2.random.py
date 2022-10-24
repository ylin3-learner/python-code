# coding:utf-8

# 小慕设计了一个小程序，模拟支付宝的集五福活动，代码以及实现效果如下

# 等以後有實力了, 再回頭優化
import random

happy = {
    "1": {"name": "富强福", "num": 0},
    "2": {"name": "和谐福", "num": 0},
    "3": {"name": "友善福", "num": 0},
    "4": {"name": "爱国福", "num": 0},
    "5": {"name": "敬业福", "num": 0}
}

print("集五福，迎新春~\n")
while True:  # 此會無限循環, 造成內存溢出
    start = input("按下<Enter>键集五福，迎新春")
    if isinstance(start, str): # 效果同: if type(start) == str:
        number = random.randint(1, 5)
        print('number', number)
        for k, v in happy.items():
            # items() 方法的遍历：items() 方法把字典中每对 key 和 value 组成一个元组，并把这些元组放在列表中返回。
            if str(number) == k:  # Todo
                print(number)
                v["num"] = v["num"] + 1
                print("获取到: {}".format(v["name"]))

        print("当前拥有的福:")
        a = 0 # 每一次循環都會把a的值初始化為0
        for k, v in happy.items():
            print(v["name"], ":", v["num"], end="\t\t")
            if v["num"] != 0: # 若字典v中每一個num的值不為0, a就加1
                a += 1
            print('a', a)
        print("\n")
    break


