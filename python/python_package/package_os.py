# coding:utf-8

# FileNotFoundError: 沒有發現文件
'''
getcwd() -- 返回當前的路徑, return str
listdir() -- 返回指定路徑下所有的文件與文件夾, var == Path返回一個列表
makedirs() -- var == Path Mode, 創建多級文件, no return; 若文件不存在, 會自動創建不存在的文件
removedirs() -- 刪除多個文件夾, no return
rename(old name, new name) -- var == old name, new name --改名
rmdir() -- 只能刪除空文件夾, no return
'''

# import os.path
'''
exists() -- 是否存在, return bool
isdir() -- 是否是目錄, return bool
isabs() -- 是否是絕對路徑, return bool
'''
'''
isfile(path) -- 是否是文件, return bool
join(path, path*) -- 路徑字符串合併, return str
split(path) -- 以最後一層路徑為基準分割, return tuple 
'''
'''
os.path.dirname() -- 返回文件路徑
os.path.basename() -- 返回文件名
os.path.join(path, name) <-> os.path.split(path)
os.path.abspath() -- 獲得絕對路徑
os.path.chdirs() -- 'change dirs'改變路徑到指定路徑
'''
import os
import os.path

current_path = os.getcwd() # 返回當前的路徑
print(current_path)
print(os.path.isabs(current_path)) # 判斷current_path是否為絕對路徑
print(os.path.isabs('animal')) # animal為相對路徑 -- False



new_path = '%s/test1' % current_path # 絕對路徑 --current path
if os.path.exists(new_path): # 判斷路徑是否存在
    os.makedirs(new_path)  # 創建多級文件

data = os.listdir(current_path) # 返回指定路徑下所有的文件與文件夾
print(data)

new_path2 = os.path.join(current_path, 'test2', 'abc') # C:\Users\user\Desktop\python\python_package --絕對路徑
print(new_path2)
print(os.path.split(new_path2)) # 分路徑的方法: '文件夾', '腳本'
if os.path.exists(new_path2):
    os.makedirs(new_path2)
if os.path.exists('test3'):
    os.makedirs('test3') # 相對路徑: 當前腳本所在的路徑

if os.path.exists('test2/abc'): # 'test2/abc' -- 相對路徑
    os.removedirs('test2/abc')
if os.path.exists('test3'):
    os.rename('test3', 'test3_new') # rename(old name, new name) -- 修改名字
if os.path.exists('pip_image.py'):
    os.rename('pip_image.py', 'pip3_image.py')  # 修改文件名字
if os.path.exists('%s/test3_new' % current_path):
    os.rmdir('%s/test3_new' % current_path)
if os.path.exists('test1'):
    os.rmdir('test1') # Directory not empty

current_path = current_path + '/package_os.py'
print(os.path.isfile(current_path)) # isfile()是否是文件
print(os.path.isdir(current_path)) # isdir() -- 是否是路徑, 判斷文件夾 >> False
print(os.path.split(current_path)) # split() -- 將最後一層和從根路徑開始的路徑切割開來
print(os.path.isdir(os.path.split(current_path)[0])) # isdir()是否是路徑

print(dir(os.path))
