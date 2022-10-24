# coding:utf-8

# 不能用findall()，findall()返回一个列表。search() 返回一个对象，然后使用group()获得匹配的值，该值为str类型。
'''
re.findall(pattern, string, flags=0)
或
pattern.findall(string[, pos[, endpos]])

pattern 匹配模式。
string 待匹配的字符串。
pos 可选参数，指定字符串的起始位置，默认为 0。
endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
'''

# 注意： match 和 search 是匹配一次 findall 匹配所有。

# re.match与re.search的区别
# re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，而 re.search 匹配整个字符串，直到找到一个匹配。

import re

test = '3.1415 9265 3589 7932 3846'
result = re.search(r'^[3]\.(\d{1,4}\s){3}', test)  # r的作用是防止字符串被转义
# >>> startswith:3, \. , [0-9](xxxx) * 3, [\t\n\f\v]
# (xxxx) => 可以從(x)-(xxxx)
# 反斜杠後面的字符將不加更改地包含在字符串中，並且所有反斜杠都保留在字符串中。例如，字符串文字 r"\n"由兩個字符組成：'\'和小寫字母'n'
print(result.group())  # 返回所有字符串

'''
^是以具体字符开头
使用()是对匹配的内容进行分组
\d是匹配的数字
[ ]是匹配括号中一个字符
\s是匹配空格
{n,m}是最少匹配n次且最多匹配m次
匹配特殊字符需用\转义
{n}是匹配指定的n次
'''

content = 'c:\\a\\b\\c'
print(content)

result_1 = re.match('c:\\\\', content).group()
print(result_1)

'''
正则表达式中使用"\"作为转义字符，如果需要匹配文本中的字符"\"，在正则表达式中需要4个"\"
前2个"\"和后两个"\"在python解释器中分别转义成一个"\"
转义后的2个"\"在正则中被转义成一个"\"
'''
result_2 = re.match(r'c:\\', content).group()  # r的作用是防止字符串被转义
print(result_2)


# 1-100中的任意数字
s = '100'
ret = re.match(r'100|[1-9]\d{0,1}$', s)  # “|”为或，匹配正则表达式100或[1-9]\d{0,1}满足一个即可匹配
# [1-9]\d{0,1}：[1-9]匹配数字1-9，\d匹配数字，\d{0,1}匹配0个或1个数字，此表达式可匹配1-99；
# $：$匹配字符串终止部分
# 100或1-99为终止
print(ret.group())


'''
小慕买了10包方便面，记录如下：
康师傅, 康帅傅, 康师傅, 康帅傅, 康帅傅, 康师傅, 康帅傅, 康师傅, 康帅傅, 康师傅
使用正则表达式帮小慕找出其中的山寨商品吧，看看一共有多少山寨货
'''

noodles = '康师傅, 康帅傅, 康师傅, 康帅傅, 康帅傅, 康师傅, 康帅傅, 康师傅, 康帅傅, 康师傅'

re_g = re.compile('康[^师]傅')  # 非 ('师')
result = re_g.findall(noodles)

print(f'山寨品為:{result}')
print(f'小慕共買了{len(result)}項山寨品')


'''
准备添加5个微信好友，手机号码如下：
131,0000,0001
131,0000,0002
131,0000,0003
131,0000,0004
131,0000,0005
编写一个程序，将手机号码中的逗号去掉
'''

import re

phone_num = '131,0000,0001, 131,0000,0002, 131,0000,0003, 131,0000,0004, 131,0000,0005'
def test(data):
    re_g = re.compile(',')
    result = re_g.sub(' ', data)
    return result

print(test(data=phone_num))

test = re.sub(r',', ' ', phone_num)
print(test)


# re.sub(pattern, repl, str, count=0, flags=0) -前三个为必选参数，后两个为可选参数。

'''
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
flags : 编译时用的匹配模式，数字形式。
'''

# re.search是无法匹配出4位长度的？
date2 = 'hioerjer hrserjs ejoesi eesoi'
print(re.findall(r'h([\w]+)e', date2))

'''
'h([a-zA-Z])e' 中[a-zA-Z]只能匹配一个a-z或A-Z的字母，可以使用'h([a-zA-Z]+?)e'进行匹配
使用+可以匹配多次
使用？则是非贪婪匹配，匹配到第一个e就结束
就可以匹配到h开头e结尾的部分
'''















