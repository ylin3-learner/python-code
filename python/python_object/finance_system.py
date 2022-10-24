# coding:utf-8

class Cat():
    # 创建构造函数
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def show_info(self):
        """ 显示猫的信息 """
        print(
            '我叫{},今年{}歲。我是{}'.format(self.name, self.age, self.color))
    def eat(self):
        """ 吃 """
        print('我喜歡吃魚')
    def catch(self):
        """ 猫捉老鼠 """
        print('我能捉老鼠')
# 创建两只猫的实例对象，并调用相应的方法
cat = Cat('花花', 2, '黑色的')
cat.show_info()
cat.eat()
cat = Cat('雪球', 3.5, '白色的')
cat.show_info()
cat.catch()


#coding: utf-8
import time

class Money_exchange(object):
    money = 0
    abstract = []
    single_bill_list = [] # 每次交易紀錄
    bill_list =[]
    transcation_num = 0 # 交易紀錄重0開始
    currency_type = "人民币"
    service_option_num = []
    service_option = []
    service_menu ={
        1: "1、存款",
        2: "2、取款",
        3: "3、查看明细",
        4: "4、查看余额",
        0: "0、退出系统"
    }
    for key, value in service_menu.items(): 
        service_option_num.append(key)
        service_option.append(value)

    def welcome_menu(self):
        print('*' * 20 + '欢迎使用资金交易管理系统' + '*' * 20)
        for i in range(0,len(self.service_option)):
            print(self.service_option[i])
        print('*' * 60)

    def save_money(self):
        self.money_to_be_save = float(input('请输入存钱金额：'))
        self.abstract = '转入'
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # 實時紀錄取出時間
        self.money += self.money_to_be_save # 存入的錢 = 現在的錢
        # 製造每筆交易的資料: time, abstract, 錢的變更, type, 變更後的錢=money
        self.single_bill_list.append(self.time)
        self.single_bill_list.append(self.abstract)
        self.single_bill_list.append(self.money_to_be_save)
        self.single_bill_list.append(self.currency_type)
        self.single_bill_list.append(self.money)
        self.bill_list.append(self.single_bill_list)
        self.single_bill_list = []  # 每次调用时先将默认的list清空，然后再进行元素添加操作, 數據才不會混雜
        self.transcation_num += 1  # 給予每次儲存的交易紀錄不同位址
        # 用戶操作提示信息
        print('已成功存入！当前余额为：%s 元' % self.money)
        input('请点击任意键以继续...')

    def withdraw_money(self):
        self.money_to_be_withdraw = float(input('请输入取出金额：')) # 避免不支持輸入小數點--float
        if self.money_to_be_withdraw <= self.money:
            self.abstract = '取出'
            self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.money -= self.money_to_be_withdraw
            self.single_bill_list.append(self.time)
            self.single_bill_list.append(self.abstract)
            self.single_bill_list.append(self.money_to_be_withdraw)
            self.single_bill_list.append(self.currency_type)
            self.single_bill_list.append(self.money)
            self.bill_list.append(self.single_bill_list)
            self.single_bill_list = []
            self.transcation_num += 1
            print('已成功取出！当前余额为：%s 元' % self.money)
            input('请点击任意键以继续...')
        else:
            print('您输入的取出金额超过余额，无法操作！请重新输入')
            input('请点击任意键以继续...')

    def check_bill_list(self):
        print('|      交易日期      |  摘要  |  金额  |  币种  |  余额  |')
        for i in range(0, self.transcation_num):
            print("|%s | %s | %s | %s | %s|" % (
                self.bill_list[i][0],  # [i]-每一條信息的self.bill_list-time
                self.bill_list[i][1],  # self.bill_list-abstract
                self.bill_list[i][2],  # self.bill_list-money
                self.bill_list[i][3],  # self.bill_list-currency_type
                self.bill_list[i][4]   # self.bill_list-money - to_be_withdraw
            ))
        input('请点击任意键以继续...')

    def check_money(self):
        print('账户余额为：%s元' % self.money)
        input('请点击任意键以继续...')

    def user_input(self):  # 用戶選擇選項
        option = float(input('请输入选项：')) # 用戶選項
        if option in self.service_option_num:
            if option == 1:
                self.save_money()
            if option == 2:
                self.withdraw_money()
            if option == 3:
                self.check_bill_list()
            if option == 4:
                self.check_money()
            if option == 0:
                print('您已成功退出，谢谢！')
                exit() # 直接跳出, exit()/quit()，跑出SystemExit異常。一般在互動式shell中退出時使用。
        else:
            print('抱歉，你输入有误，请重新输入！')
            input('请点击任意键以继续...')

money_exchange = Money_exchange()
while True:
    money_exchange.welcome_menu()
    money_exchange.user_input()
