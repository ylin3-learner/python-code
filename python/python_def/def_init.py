# coding: utf-8

'''
def name(argu):
    todosth
    return 變量值 --> 代表函數的結束, 也就代表即便後面有程序也無法執行, 並將返回值到函數以外
'''


def capitalize(data):   # for loop str, and make the first ch become capital
    index = 0  # 要使電腦知道何為str的第一個字母, 默認為0
    temp = ''  # 因為字符串自身不能修改, 需要定義一個新字符串去接受修改後的新str

    for item in data:
        if index == 0:
            temp = item.upper()
        else:
            temp += item
        index += 1
    return temp
    print('finish')

result = capitalize('hello 小慕')
print(result)


def message(message, message_type):
    new_message = '[%s] %s' % (message_type, message)
    print(new_message)

result = message(message='今天天氣真好!', message_type='info')
print('message result', result) # 輸出結果: result=None, 他沒有返回值
# print --單純打印, 不支持賦值 vs. result --結果返回, 支持賦值

def test():
    for i in range(10):
        if i == 5:
            return i  # 在函數中效果相當於break

print('test 結果是:', test())