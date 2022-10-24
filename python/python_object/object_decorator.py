# coding:utf-8

def check_str(func):
    print('func:', func)  # **kw定義關鍵引數，代表任意引數
    def inner(*args, **kwargs): # 內傳入外圍函數的參數 func 對應的參數 -- *args, **kwargs
        print('args:', args, kwargs)
        result = func(*args, **kwargs)  # 在內嵌中調用函數參數, 將參數放回函數
        if result == 'ok':
            return 'result is %s' % result
        else:
            return 'result is failed: %s' % result
    return inner # 外圍函數返回內嵌函數—因為所有的業務都在內, 不返回則無法調用

@check_str
def test(data):
    return data

result = test(data='no') # 返回字典類型
print(result)

result = test(data='ok')
print(result)
