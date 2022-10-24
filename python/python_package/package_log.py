# coding:utf-8

'''
日誌的等級:
    debug
    info
    warning
    error
    critical
'''


'''
logging模塊的使用:
    logging.basicConfig
        var -- level日誌輸出的等級, 低於level將無視, format格式, filename存儲位置, filemode輸入模式
'''
'''
format:
    %(levelname)s, %(pathname)s, %(filenames)s, %(linenos)d日誌當前行號(數字類型), %(asctime)s打印日誌的時間
    %(message)s日誌信息
format = '%(asctime)s %(filename)s [line:%(linenos)d] %(levelname)s %(message)s'
'''

import logging
import time
import os

# DEBUG -> 對應初始化等級, 代表DEBUG以下的等級不會被記錄; debug -> 對應函數

def init_log(path): # path存入日誌的文件與地址
    # if os.path.exists(path):
    #     mode='w'
    # else:
    #     mode='a'

    mode='a' if os.path.exists(path) else 'w' # 三元運算中賦值式只能作為左值

    logging.basicConfig(
        level = logging.INFO,  # 對應初始化等級, INFO以下會被忽略
        format = '%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',
        filename = path,  # 存到日誌中
        filemode = mode  # 因為文件不存在, 使用'w'; 反之, 使用'a'
    )

    return logging # 返回logging模塊

current_path = os.getcwd()
path = os.path.join(current_path, 'first_log')
log = init_log(path) # 將init_log賦值給log, 並在之後調用log屬性


log.info('這是紀錄的第二個日誌信息')
time.sleep(2)
log.warning('這是一個警告')
time.sleep(2)
log.critical('這是一個重大的錯誤信息')
logging.debug(1)