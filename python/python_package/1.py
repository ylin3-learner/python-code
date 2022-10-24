# coding: utf-8

count = 1
while count < 100:
    count += 1
print(count)

# 當我們要傳入大量的參數時，在函式上定義過多的參數名稱會讓程式碼的可讀性降低，這時候就可以使用 * 符號來將傳入參數進行打包
'''
* 將參數資料打包成元組(Tuple)
** 打包成字典(Dictionary)資料型態
'''


# 想要透過函式來修改全域變數的值，則可以使用 global 關鍵字
'''
非必要避免在函式中修改全域變數的值，
因為永遠不會知道程式的其他地方有沒有使用了這個全域變數來進行運算，
而在函式中修改了它的值後，很容易導致程式的副作用(Side Effect)或錯誤(Bug)。
'''

x = 100

def test():
    global x
    x = 20
    return x

print(test())

'''
Python的函式都有回傳值:
用一個變數來接無回傳值函式的結果時，從執行結果可以看到Python隱含回傳了一個None
在函式中沒有使用 return 關鍵字回傳結果，所以在來源端用一個變數來接回傳值時，會得到None(也就是此函式無回傳值的意思)
'''
from functools import reduce
def test_2():
    global x
    res = reduce(lambda x,y: x+y, map(lambda x: x ** 2, [2, 4, 6]))
    print(res)

print(test_2())

l = {'a': 1, 'b': 2, 'c': 5}  # 字典的key必须为字符串类型，并且选项中的key与参数名相同
def calc(a, b, c):
    return (a + b) * c

print(calc(**l))

a = 5
b = 4
c = 9
d = 2
try:
    if not (a > b and b > c):
        print(c/(b % d))  # ZeroDivisionError: division by zero
except Exception as e:
    print(e)
else:
    print(c - 1 == 1)
'''
    raise e('不能被0整除')
    關鍵字 (keyword) raise 用來發起例外 (exception) 
    所謂例外是指已知有可能發生的錯誤 (error) ，只要程式 (program) 執行過程中發生例外
    程式就會中斷執行，並且在命令列上印出錯誤訊息。
'''


# 打印的是将res强制转化为list后的结果
# res是map对象而非list类型
test_ls = [32, -3, 10, -8]
res = list(map(lambda x: x+1, test_ls))
print(res)

# 將傳入的函數依次作用於序列中的每一個元素, 返回指定函數的返回值 - map => 映射

'''
reduce() 函数会对参数序列中元素进行累积
reduce() 第一个参数是函数，第二个是序列（列表或元组）。但是，其函数必须接收两个参数
reduce()对list的每个元素反复调用函数，并返回最终结果值
'''

print('imooc' != 'mooc')
print(12 == 12.0)
print(19 <= 12)

print(18 == True) # 結果為False, 因為True只能對應數值1; 而False對應數值0

print('--------')
print(0 == False)
print(1 == True)
print(2 == True) # 結果為False, 因為True只能對應數值1; 而False對應數值0
print(bool(18))
print(bool(True))