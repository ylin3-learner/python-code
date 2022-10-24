# coding:utf-8

import sys
import random
from datetime import datetime



class Guess_the_Number(object):
    def __init__(self):
        pass

    def guide_page(self, guide_word):  # 自定义游戏进入提示函数guide_page(guide_word)：
        self.guide_word = guide_word
        print('*' * 30 + '{}'.format(guide_word) + '*' * 30)

    def all_num(self, n):  # 自定义数字类型判断函数all_num(n)
        self.n = n
        # 自定义数字类型判断函数all_num(n)：
        return n if self.n.isdigit() else print('您所輸入的為非數字字符, 請重新輸入')  # 方法检测字符串是否只由数字组成。 str.isdigit()
        # 输出使用print( )，input( )时输入
    def num_legal(self, ls):  # 自定义数值合法性判定函数num_legal(ls)
        self.ls = ls
        if int(ls[0]) == int(ls[1]):
            print('您輸入的區間數字相同, 請重新啟動程序')
        elif int(ls[0]) > int(ls[1]):
            print('您輸入的區間大小有誤, 請重新啟動程序')
        else:
            return 1
        sys.exit()

    def set_final_num(self, num1, num2):  # 自定义产生指定区间随机数函数set_final_num(num1,num2)
    # 利用内置函数filter()及思路分析2中的all_num(n)过滤以确保输入值全部为数字
        filter_result = list(filter(self.all_num, [num1, num2]))
    # 若全部为数字，则调用自定义的等值判断函数，判断输入值是否相等，并根据判断之后的返回值，输出用户产生随机数的区间
        if len(filter_result) == 2:
            result = self.num_legal(filter_result)
            if result == 1:  # 返回1表示數字區間沒問題
                print('所產生的隨機數字區間為: %s' % filter_result)
                return random.randint(int(num1), int(num2))
        else:
            print('您所輸入的為非數字字符, 請重新啟動')
            sys.exit()

    def check_num_legal(self, num): # 自定义核查数值是否属于指定区间函数
        if int(num) < int(self.ls[0]) or int(num) > int(self.ls[1]):
            print('對不起您輸入的數字未在指定區間!!!')
            return 1

    def write_record(self, times, value):  # 将玩家每一次猜测数字和本次猜测次数两项信息写入日志文件
        value = f'第{times}次您猜測的數字為:{value}'
        now = datetime.now()
        with open('record.txt', mode='a', encoding='utf-8') as f:
            f.write(f'{now}{value}\n')

    def main(self, rand1):
        temp = 0
        while True:
            guess_num = input('請繼續輸入您猜測的數字:')
            # 判斷猜測數字是否為數字類型
            if self.all_num(guess_num):
                guess_num = int(guess_num)
                # 判斷猜測數字是否在指定區間
                if self.check_num_legal(guess_num):
                    continue
                temp += 1
                # 調用日誌寫入函數, 傳入猜測的數字和用戶猜測的數字
                self.write_record(temp, guess_num)
                print('*' * 20)
                # 判斷猜測數字與隨機數字的比較
                if guess_num > rand1:
                    print('Higher than the answer')
                elif guess_num < rand1:
                    print('Lower than the answer')
                else:
                    print(f'恭喜您只用了{temp}次就贏了遊戲')
                    break

if __name__ == '__main__':
    guess_the_number = Guess_the_Number()
    # print(guess_the_number.guide_page(guide_word='歡迎進入數字猜猜猜小遊戲'))
    '''
    在print( )函数中调用函数会输出返回的返回值，
    guide_page( )函数没有返回值会输出None，在代码中直接调用guide_page函数就可以，不用输出。
    '''
    guess_the_number.guide_page(guide_word='歡迎進入數字猜猜猜小遊戲')
    i = input('數字區間起始值:')
    j = input('數字區間終止值:')
    rand1 = guess_the_number.set_final_num(i, j)
    guess_the_number.main(rand1)
