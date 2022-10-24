# coding:utf-8

'''
sys.modules -- return list, python啟動時加載的模塊
sys.path -- return list, python當前的環境路徑(所有可導入的第三方包/函數的路徑)
sys.exit(arg) -- no return, 退出程序; type(arg) == int
sys.getdefaultencoding() --獲取系統編碼, return str
'''
'''
sys.platform -- return str; platform只是屬性, 不是函數
sys.version -- 獲取python屬性, return str
sys.argv -- var == *args, 程序外部獲取參數; return list
'''
# Windows电脑一般使用python  py文件名命令

import sys

command = sys.argv[1]
if command == 'modules':
    modules = sys.modules # python啟動時加載的模塊
    print(modules)
elif command == 'path':
    path = sys.path # sys.path -- return list, python當前的環境路徑(所有可導入的第三方包/函數的路徑)
    print(path)

# sys.exit(1) # 进程已结束,退出代码1
elif command == 'encoding':
    code = sys.getdefaultencoding()
    print(code)
elif command == 'platform':
    print(sys.platform) # 返回系統名 >> win32
elif command == 'version':
    print(sys.version)
else:
    print('not command')
print(sys.argv) # 用于获取命令行参数列表，这里获取的参数是从程序外部输入的