# coding:utf-8

'''
hashlib: 難破解, 不可逆
    md5(byte), return hash object
    sha1(byte), return hash object
    sha256(byte), return hash object
    sha512(byte), return hash object
        hashobj = hashlib.md5(b'hello')
        result = hashobj.hexdigest()
        print(result)
'''

import hashlib
import time

base_sign = 'mooc'  # A, B兩方都使用相同的電子簽


def custom(): # 客戶端
    a_timestamp = int(time.time()) # time.time() -- float
    _token = '%s%s' % (base_sign, a_timestamp)

    hashobj = hashlib.sha1(_token.encode('utf-8'))  # 轉換為byte類型
    a_token = hashobj.hexdigest()  # hexdigest()生成16進制字符串
    return a_token, a_timestamp

def b_service_check(token, timestamp):  # 檢查 -- 請求方驗證的token, 時間戳
    _token = '%s%s' % (base_sign, timestamp)
    b_token = hashlib.sha1(_token.encode('utf-8')).hexdigest()  # var == bite
    return _token == b_token
'''
return _token == b_token 與下方程式碼邏輯相同

if _token == b_toke:
    return True
else:
    return False
'''

if __name__ == '__main__':
    need_help_token, timestamp = custom()
    time.sleep(1)
    result = b_service_check(need_help_token, int(time.time())) # timestamp--使用a服務帶來的時間戳
    print('a合法, b服務可以進行幫助') if result == True else print('a不合法, b不可進行幫助')
'''
if result == True:
    print('a合法, b服務可以進行幫助')
else:
    print('a不合法, b不可進行幫助')
'''