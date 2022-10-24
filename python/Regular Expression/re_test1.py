# coding:utf-8

# 如何返回複數

import re

def had_num(data):
    result = re.findall('\d', data)  # 如果data中有數字, result就不會為空, 會進入到for loop
    # \d -任意十進位數字
    print(result)
    # 判斷列表是否為空
    for i in result:
        return True

    return False

    # return len(data) != 0
'''
取代 if len(data) != 0:
        return True
    else:
        return False
'''

def delete_num(data):
    result = re.findall('\D', data)  # \D -non int
    print(result)
    return ''.join(result)  # 將列表轉回字符串

def startswith(sub, data):  # 要判斷的開頭字符-sub, data為完整字符
    _sub = '\A%s' % sub
    result = re.findall(_sub, data)
    return len(result) != 0

def endswith(sub, data):
    _sub = '%s\Z' % sub   # \Z -結尾, 如同endswith
    print(_sub)
    result = re.findall(_sub, data)
    print(result)
    for i in result:
        return True  # 在for循環中, 只要出現return, 將只執行一次循環

    return False

def real_len(data):
    result = re.findall('\S', data)
    print(result)
    return len(result)

if __name__ == '__main__':
    data = 'I am Tony,and I am 19'
    result = had_num(data=data)
    print(result)
    result_2 = delete_num(data=data)
    print(result_2)

    data_2 = 'hello xiaomu, I am dewei. I am 33 year\'sold'
    print(re.findall('\W', data_2))

    result = startswith(sub='shell', data=data)
    print(result)


    print(endswith(sub='olds', data=data_2))

    print(len(data_2))
    print(real_len(data_2))