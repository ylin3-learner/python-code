# coding:utf-8

# 序列化: info transfer to 傳輸,存儲 -> str
# 可序列化: number, str, list, tuple, dict(最常用的)
# 不可序列化: set, def, set
'''
json modules
dumps: 對象序列化, var == obj, return str
loads: 反序列化, var == str, return 原始序列類型

json不認識tuple, 所以序列化後變成list; 就算反序列, 也無法變回tuple
'''
'''
pickle modules
pickle.dumps: 對象序列化, var == obj, return bite
pickle.loads: 反序列化, var == str, return 原始序列類型
'''

import json

def read(path):
    with open(path, mode='r', encoding='utf-8') as f:
        data = f.read()

    return json.loads(data) # 反序列化: 將數據變為原本的數據類型

def write(path, data): # type(data) == dict
    with open(path, mode='w', encoding='utf-8') as f:
        if isinstance(data, dict): # 判斷數據是否為某種數據類型
            _data = json.dumps(data) # 將數據類型變為str
            f.write(_data) # 將message=_data傳入path
        else:
            raise TypeError('data is dict') # 有錯, 自定義錯誤信息

    return True # 給最外圍的with open()判斷必定為真

data = {'name': '小木', 'age': 18, 'top': 176}

if __name__ == '__main__':
    write(path='test.json', data=data)

    result = read(path='test.json')
    result['sex'] = 'boy'
    write(path='test.json', data=result)
    print(result, type(result))