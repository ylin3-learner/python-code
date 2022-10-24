# coding: utf-8

username = '小慕'
get_up_time = '8:00'
bf_time = '8:30' # 早餐時間
bf_contents = ['麵包', '牛奶', '麥片']
learn_time = '9:00'
books = ('高等數學', '歷史', 'python入門')
learn_book = 'python入門'
ready_lunch_time = '12:00'
brother_phone = 123456789
real_lunch_time = '12:55'
lunch_pay = 12.5
lunch_name = '西紅柿雞蛋蓋飯'
shopping_time = '1:25'

shop = {
    'snacks': ('薯片', '鍋巴', '餅乾'),
    'life': ['洗髮', '香皂', '沫浴乳'],
    'fruits': ['apple', 'banana', '哈密瓜', 'orange', 'watermelon'],
    'vegetables': ['tomato','黃瓜', '韭菜', '大白菜'],
    'drinks': ['soda', 'coke', 'water']
}

a, b, c = 5, 10, 15
coke_pay = 2.5
potato = 4
two_apples = 1.2
cabbage = 0.9

total = coke_pay + potato + two_apples + cabbage + c
sport_time = 2.5
before_weight = 44.78
after_weight = 44.76
back_home_time = '5:00'

if __name__ == '__main__':
    print('character is:', "小慕")
    print('他是', get_up_time, '起床')
    print(bf_time, '吃早餐')
    print('早餐有:', bf_contents)
    print(learn_time, '開始學習')
    print('書架上有:', books)
    print(username, 'read', learn_book)
    print(username, 'prepare', lunch_name, 'for lunch')
    print('Deliverman phone number is:', brother_phone)
    print(username, 'actually eat at', real_lunch_time)
    print('What he ate is:', lunch_name, 'and its price is:', lunch_pay)
    print('購物時間是:', shopping_time)
    print('超市的櫃檯裡有:', shop)
    print(username, 'total cost is:', total, 'dollars')
    print('去健身了')
    print('健身之前, 體重是:', before_weight, 'kg')
    print('經過了:', sport_time, 'hr')
    print('現在體重是:', after_weight, 'kg')
    print(username, '在', back_home_time, '回家了')


