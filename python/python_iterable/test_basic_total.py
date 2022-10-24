# coding: utf-8

# 注意货币单位的使用人民币为￥，美元为$，欧元为€
# 三个货币兑换服务是不同的, 所以应先选择服务后才能输入相应服务需要输入的货币金额，进行转换，并不是每次都是输入人民币
rnb = '人民幣'
us = '美元'
eu = '歐元'
intro = '歡迎使用{}轉換{}服務\n'
service_menu = {
    1: '人民币转换美元',
    2: '美元转换人民币',
    3: '人民币转换欧元',
    0: '结束程序'
}
while True: # 程序只要不退出是一直循环的，可以使用while True 死循环，直到输入0时使用break跳出循环
    print('*' * 10 + '歡迎使用貨幣轉換服務系統' + '*' * 10)
    for key, value in service_menu.items():
        print('{}.{}'.format(key, value))
    Your_choice = int(input('請您選擇需要的服務:'))
    if Your_choice == 1:
        print('~' * 21)
        print(intro.format(rnb, us))
        your_money = int(input('請您輸入需要轉換的人民幣金額:'))
        print(f'您需要轉換的人民幣為:{your_money}')
        result = '兌換成%s為:%.2f￥'
        RMB_to_US = your_money / 6.36
        print(result % (us, RMB_to_US))
        print('='.zfill(22).replace('0', '='))
    elif Your_choice == 2:
        print('~' * 21)
        print(intro.format(us, rnb))
        your_money = int(input('請您輸入需要轉換的人民幣金額:'))
        print(f'您需要轉換的人民幣為:{your_money}')
        result = '兌換成%s為:%.2f$'
        US_to_RMB = your_money * 6.36
        print(result % (rnb, US_to_RMB))
        print('='.zfill(22).replace('0', '='))
    elif Your_choice == 3:
        print('~' * 21)
        print(intro.format(rnb, eu))
        your_money = int(input('請您輸入需要轉換的人民幣金額:'))
        print(f'您需要轉換的人民幣為:{your_money}')
        result = '兌換成%s為:%.2f€'
        RMB_to_EUR = your_money / 7.1
        print(result % (eu, RMB_to_EUR))
        print('='.zfill(22).replace('0', '='))
    elif Your_choice == 0:
        print('~' * 21)
        print('感謝你的使用, 祝您生活愉快, 再見!')
        break
    else:
        print('service\'input error')

