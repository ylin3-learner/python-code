# coding:utf-8

'''
try:
    <code1> # 被try檢查並保護的業務代碼
except(異常的類型):
    <code2> # code1 出現錯誤後的代碼塊
'''
'''
try: 
    1 / 0
except:
    print('0不能被1整除')
    print('程序繼續執行')
'''

def upper(str_data):
    new_str = ''
    try:
        new_str = str_data.upper()
    except Exception as e:
        print('coding went wrong: %s' % e)
    return new_str

result = upper('dewei')
print(result)
result = upper(1)
print('result:', result)

# 捕獲通用異常: unsure error
'''
try: 
    code
except Exception as e: # convert Exception into e(nickname of Exception)
    print(e)
'''

# 具體異常 -- except 具體的異常類型 as e:
'''
try: 
    1 / 0
except ZeroDivisionError as e:
    print(e)
'''

def test():
    try:  # 如果try中的code有錯, 不管下方還有沒有代碼, 直接進入except的代碼塊
        print(float(123))
        1 / 0
        print('hi')
    except (ZeroDivisionError, NameError) as e:
        print(e)
        print(type(e))
        print(dir(e))

test()

def test1():
    try:
        print('test')
        print(name)
    except NameError as e:
        print(f'Error is:\n {e}')

test1()

# 捕獲多個異常
'''
1. 疊加多個except, 不過這時; 當捕獲到第一個以後, 不會繼續往下捕獲
2.  except (NameError, ZeroDivisionError,...) as e: 用元組包裹, 捕到哪種拋哪種
'''
