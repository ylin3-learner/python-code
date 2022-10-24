# coding:utf-8

# 內置函數open(path: 文件路徑, mode:操作模式), return 文件對象 -->生成對象,進行創建,讀寫操作
# f = open('d:\\.txt', 'w') 'w' == write

'''
mode = [
 {w: 創建文件}, # 若已有, 將會覆蓋內容 -- 寫入字符串
 {w+: 創建並讀取文件}, # 若已有, 不會覆蓋內容
 {wb: 二進制形式讀取文件},# 若已有, 將會覆蓋內容 -- 寫入比特類型 b'str'
 {wb+: 二進制形式創建或追加內容},
 {a: 追加內容},
 {a+: 讀寫模式的追加},
 {ab+: 二進制形式讀寫追加} # 追加並讀取比特類型
]
'''
'''
文件對象的操作方法 = [
 {write(var == message): 寫入信息},
 {writelines(var == message_list): 批量寫入信息},
 {close(): 關閉並保存文件}
]
操作完成後, 必須使用close方法
'''

# Window系統在寫入中文時需要設置編碼格式, 例如: f = open(xxx + '/'+'x.txt','w',encoding='utf-8')
# 若文件中有中文是需要设置编码格式的
'''
+	打開一個文件進行更新(可讀可寫)
r	以只讀方式打開文件
r+	打開一個文件用於讀寫, 文件指针会放在文件之前
w	打開一個文件只用於寫入，如果該文件已存在則打開文件，並從開頭開始編輯，原有內容會被刪除。如果該文件不存在，創建新文件。
w+	打開一個文件用於讀寫。如果該文件已存在則打開文件，並從開頭開始編輯，原有內容會被刪除。如果該文件不存在，創建新文件。
a	打開一個文件用於追加。如果該文件已存在，新的內容將會被寫入到已有內容之後。如果該文件不存在，創建新文件進行寫入。
a+	打開一個文件用於讀寫。如果該文件已存在，文件指針將會放在文件的結尾。文件打開時會是追加模式。如果該文件不存在，創建新文件用於讀寫。
ab+	以二進制格式打開一個文件用於追加。
'''
import  os

def create_package(path): # 自動創建python的包
    if os.path.exists(path): # 判斷path是否存在
        raise Exception('%s 已經存在不可創建' % path)
    os.makedirs(path) # makedirs() -- var == Path Mode, 創建多級文件, no return; 若文件不存在, 會自動創建不存在的文件
    init_path = os.path.join(path, '__init__.py') # join(path, path*) -- 路徑字符串合併, return str
    f = open(init_path, 'w') # w -- 打開一個文件只用於寫入，如果該文件已存在則打開文件，並從開頭開始編輯，原有內容會被刪除。如果該文件不存在，創建新文件。
    f.write('# coding:utf-8\n')
    f.close()

# 如果message本身是以\n结尾的，那就不会执行if not message.endswith('\n')语句，直接执行f.write(message)
# 如果message不是以\n结尾，就执行if中的message = '%s\n' % message语句，为message添加\n结尾
# 写入到b.txt中的内容最后一行也会空行，因此这里不用else是可以的，不会出问题，文件写入使用try捕获异常写法正确
class Open(object):
    def __init__(self, path, mode='w', is_return=True): # is_return 換行符
        self.path = path
        self.mode = mode
        self.is_return = is_return

    def write(self, message):
        f = open(self.path, mode=self.mode, encoding='utf-8')
        if self.is_return: # self.is_return == True
            if not message.endswith('\n'): # message.endswith('\n') == False 才在後方加入\n
                message = '%s\n' % message
        try:
            f.write(message)
        except Exception as e:
           print(e)
        finally:
            f.close()

    def read(self, is_strip=True):  # is_strip=True -- 將每行結尾的換行符去掉
        result = []
        with open(self.path, mode=self.mode) as f: # f將自動被with關閉,省去f.close()
            data = f.readlines()

        for line in data:
            # 若is_strip值為True,則把文件中每一行的換行符即'\n'去掉
            if is_strip == True:
                temp = line.strip()
                # 去掉換行符即'\n'之後, 若temp的值不是空字符串
                # 將temp添加到列表result中

                # is_strip=True
                if temp != '':
                    result.append(temp)
            #  若is_strip值不為True
            else:
                # 則判斷每一行的內容是否為空字符串
                # 若不是空字符串, 將line添加到列表result中
                if line != '':
                    result.append(line)
        return result



if __name__ == '__main__':
    current_path = os.getcwd() # 打開一個文件只用於寫入，如果該文件已存在則打開文件，並從開頭開始編輯，原有內容會被刪除。如果該文件不存在，創建新文件。
    # path = os.path.join(current_path, 'test1')
    # create_package(path) # 調用create_package
    # open_path = os.path.join(current_path, 'b.txt')
    o = Open('package_datetime.py', mode='r')
    # o.write('你好, 小木')
    data = o.read(is_strip=True)
    print(data)