# coding:utf-8

'''
python_package: pyyaml
yaml格式: 文本文件 -- xxx.yaml
服務配置文件
key:
    value
key2:
    list
key3:
    dict

pip install pyyaml
import yaml
'''

'''
讀取yaml的方法: 
    f = open(yaml_file, 'r', encoding='utf-8')
    data = yaml.load(f.read()) # 讀取文件內容傳入反序列模塊
    f.close() # 關閉文件
  *************************
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.load(f.read()) --  # 返回字典類型: {'name: 'xiaomu', 'age': 18...}
    return data
'''

import yaml

def read(path):
    # encoding="utf-8"是指定以utf-8编码打开文件，当文件的数据是utf-8编码，也要指定以utf-8编码打开文件，否则可能会报错
    # 若文件中有中文是需要设置编码格式的
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    result = yaml.load(data, Loader=yaml.FullLoader)
    # Loader = yaml.FullLoader使data解析變得更安全
    return result

if __name__ == '__main__':
    result = read('muke.yaml') # 傳入相對路徑
    print(result, type(result))
    print(dir(yaml))