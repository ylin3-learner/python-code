# coding:utf-8

class ShortInputError(Exception): # 自定義異常類
    def __init__(self, length, atleast): # 自定義異常錯誤信息
        self.length = length
        self.atleast = atleast

def main(text):
    try:

        if len(text) < 5:
            raise ShortInputError(len(text), 5)
    except ShortInputError as result: # 將ShortInputError賦值給result
        print(f'ShortInputError:輸入的長度{result.length}, 長度至少是{result.atleast}')

    else: # 與if同層的結構
        print('沒有異常的發生')

    finally:
        print('輸入的字符串是:{}'.format(text))

main('abcd')

# 最多只會執行其中一個if, 只要滿足一個, 就不會向下執行了
'''
if 條件式 1:
    # 語句...
elif 條件式 2:
    # 語句...
elif 條件式 3:
    # 語句...
.
.
# 上述條件式都不成立執行
else:
    # 語句...
'''

# phone_num=135874125B
class MyException(Exception):
    pass

def func():
    global phone_num
    phone_num = input('請輸入手機號:')
    if not phone_num.isdigit(): # isdigit()方法用于检测字符串是否仅由数字组成 --return True
        raise MyException('手機號碼含非數字')
    if len(phone_num) != 11:
        raise MyException('手機號長度不夠')

try:
    func()
except MyException as result:
    print(result)

else:
    print('手機號為:{}'.format(phone_num))

func()

'''
try:
    可能發生例外的程式碼 (code)
except Exception as e:
    做相對應的例外處理
else:
   處理例外沒有發生的情況
finally:
    must_do
'''