# coding:utf-8

# pattern -匹配規則, string -需要匹配的字符串, [,flags] -
'''
findall(pattern, string, [,flags]) -return all matches of string, and put them into a list
search(pattern, string, flags=0) -return the first match of string. if it works, return object, else return None
與search() 相關的函數 -group(num), groups()

group(num) -返回整個匹配對象, 或編號為num的特定子組;  num 從1開始
groups() -返回一個包含所有匹配子組的元組, 如果沒有匹配成功, 則返回一個空元組

result = re.search('hello (.*) my name is (.*)', data)
result.groups() >>> ('my', 'dewei')

result.group(1) >>> ('my')
result.group(2) >>> ('dewei')

split(pattern ,string, max=0) -正則替換, max=0代表能匹配到所有能匹配的信息

data = 'hello world'
re.split('\W', data)  # \W -特殊字符, 所以匹配到空格, 並透過它進行切割列表
>>> ['hello', 'world']


match(pattern, string, flags=0) -只會匹配pattern重頭開始的信息
如果成功, 返回匹配對象, else: return None
並且匹配對象也可以通過group()調用
data = 'hello world'
result = re.match('hello', data)
result.group() >>> 'hello'

compile(pattern, flags=0) -將原本pattern的字符串, 變成一個匹配規則的對象, 之後只要調用對象傳入string就可以返回相應的信息了

data = 'hello my email is dewei@imooc.com i like python'
re_obj = re.compile('email is (.*?) i')
result = re.obj.findall(data)
print(result) >>> ['dewei@imooc.com']
'''
import re

'''
re 額外的匹配要求：flags
re.I, re.IGNORECASE -不區分大小寫的匹配
re.L, re.LOCAL -根據本地語言環境通過 [\w, \W, \s, \S] 實現匹配 --unicode-python2時代, 理解為通用模式utf-8
re.M, re.MULTILINE - ^和$分別匹配字符串中的 行的起始和結尾, 而不是整個字符串本身的起始
re.S, re.DOTALL - '.'(點號) 通常匹配除了\n(換行符)以外的所有單個字符, 並在此基礎上增加\n的匹配
re.X, re.VERBOSE - 忽略正則表達式中的空白和注釋
'''

html = ('<div class="s-top-nav", style="display:none:">'  # 希望獲取style="display:none:"
        '</div><div class="s-center-box"></div>')


def check_url(data):
    re_g = re.compile(r'[a-zA-Z]{4,5}://\w*\.*\w+\.\w+')
    print(re_g)
    result = re_g.findall(data)
    return len(result) != 0

def check_html_data(html):
    re_g = re.compile('="(.*?)"')  # 因為匹配裡只匹配了一個組的信息
    print(re_g.search(html).groups())
    re_g_good = re.compile('<div class="(.*?)", style="(.*?)">'
                            '</div><div class="(.*?)"></div>')
    print(re_g_good)

    print(re_g_good.findall(html))
    print('------')
    print(re_g_good.search(html).groups())
    print(re_g_good.search(html).group(1))

    re_g_split = re.compile('\s')
    result = re_g_split.split(html)
    print(result)

    re_g_test = re.compile('class="(.*?)"')
    result = re_g_test.match(html)
    print(result)  # 為何返回None?  因為match() -會從字符串的頭開始匹配, 而html的頭: <div ..., 所以class=..不是頭
    # 返回None
    print('----------')
    re_g_2 = re.compile('<div class="(.*?)"')
    result = re_g_2.match(html)
    print(result.groups())
    print(result.span())
    print(html[:22])



check_url(data = r'https://www.imooc.com')
check_html_data(html)