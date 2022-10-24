# coding:utf-8

# 必傳參數 -- 沒有默認值, 必須在函數執行時傳入進去, 且順序與參數同
# 默認參數 -- 含有默認值(通過賦值語句) e.g. def add(a=必傳參數, b=2 默認參數), 如果默認參數有新的值, 將優先使用新值
# 不確定參數(可變參數) -- 沒有固定名和數量, 將無參數的值合併元組, 將有參數與賦值語句合併成字典
# 參數規則: (a, b, *args, **kwargs) --必傳參數, 默認參數, 可變元組參數?, 可變字典參數

'''
形參(def函數中的參數)

實參(調用函數傳入的參數)--要有實值

位置參數: 位置一一對應

默認參數: 未傳參, 已默認值為準-->默認參在位參之後

關鍵參數: 指定參數名, 可不按順序 --> 關鍵參在位參之後

非固定參數: 同時指定多個用戶, 將傳參打包成元組或字典(name/key=value)
'''

def add(a, b, c=3): # c=3
    return a+b+c

result = add(1, 2) # a, b = 1, 2
print(result)

result = add(1, 2, 6)  # c=6 優先使用新值6
print(result)

def test_argus(*argus, **kwargs):
    print(argus, type(argus))
    print(kwargs, type(kwargs))

test_argus(1, 2, 3, 4, 5, 6, name='dewei', age=33, top=174 )

def test_argus_super(*argus, **kwargs): # \*  將無參數名的值包裹, 封裝成元組 --並不代表接收元組類型
    if len(argus) >= 1:
        print(argus[0])

    if 'name' in kwargs:
        print(kwargs['name'])
    else:
        print('no name')
    print(argus, len(argus))
    print(kwargs, len(kwargs))

test_argus_super(1, name='dewei')  # argus=1, kwargs == name='dewei'
a = ('python', 'django')
b= {'name': 'dewei'}
test_argus_super(*a, **b) # 無法透過變量名傳參, 如果想要則使用對應的\* or \**-- *argus, **kwargs,但函數體內不能加,只有傳參過程中才能加


print('=' * 30)


def add(a, b=1):
    print(a+b)

add(1, 2)
add(1)
add(a=1, b=2)
add(b=2, a=1)
# add(b=2)--會報錯

def test(a, b=1, *args):
    print(a, b, args)

s = (1, 2)
test(1, 2, *s)
# test(a=1, b=2, *s) # test() got multiple values for argument 'a' --順序應改為: *s, a, b=1

def test2(*args, a, b=1):
    print(a, b, args)

test2(a=1, b=2, *s)
s = (1, 2)

def test3(a, b=1, **kwargs):
    print(a, b, kwargs)

test3(1, 2, name='dewei')
test3(a=1, b=2, name='dewei')
test3(name='dewei', age=33, a=1, b=2)


d = {'name': '小慕'}
test3(a=1, b=2, **d)
test3(**d, a=1, b=2)