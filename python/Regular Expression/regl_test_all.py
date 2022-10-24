# coding:utf-8

# group和groups是兩個不同的函數，他們都是搭配search和match後的匹配對象來使用
# search -模式只出現了一次（當然也就是第一次出現模式)  vs.  不是出現在第一個字母開始的，不能用match
# search( )使用可选标记搜索字符串中第一次出现的正则表达式模式，匹配成功，返回匹配对象 -search( )进行匹配时，会对整个字符串进行匹配
# findall如果搭配小括號分組的話由於同樣會只返回小括號裏的內容
# -可以采用非捕獲組(非編號組)的方式, 如果字串重複出現  -(?:表達式)

# 贪婪模式是尽可能多的匹配，非贪婪模式是以最少的匹配字符，默认情况是贪婪模式

import re
import random

text = 'hello ! Imooc'
pattern = re.compile(r'imooc', re.I)  # re.compile() -創建表達式對象
res_search = pattern.search(text)  # 返回re.Match object
print(res_search.group(0))

res_match = pattern.match(text)  # 返回re.Match object -但要求匹配對象須在開頭位置
print(res_match)

print('------')

p = re.compile(r'(\d)-(\d)-(\d)')
s = p.match('2-3-1')
print(s.group())  # 返回正則表達式所有內容 -group() == group(0)
print(s.group(1), s.group(2), s.group(3))  # 返回結果1, 結果2, 結果3
print(s.groups(), s.groups(1), s.groups(2), s.groups(3))  # 返回所有匹配結果, 以元組形式 -不管groups(n), n為多少
# print(s.findall(p))  # re.Match' object has no attribute 'findall'
print(p.search('2-3-1').groups())
print(re.search('(\d)+', '2-3-1').group())


print('-------')

content_3 = '18c5H901i3n7a0'
pattern_3 = re.compile(r'[a-z]+', re.I)
print(pattern_3.search(content_3).group())
print(pattern_3.findall(content_3))

print('-------')

# 使用非贪婪模式（不区分大小写）
# 正则表达式为i.*?n

word = 'I like python, i must learn python well'
res = re.compile('i.*?n', re.I)  # 非貪婪模式 -使用最少的字符匹配
res_new = re.compile('i.*n', re.I)  # 貪婪模式
print(res.findall(word))
print(res_new.findall(word))

print('-------')

pat_new = re.compile(r'OH', re.I)
rest = pat_new.match('oh, ye')
print(rest.string)  # 匹配成功对象的string属性得到的是匹配时使用的字符串



