# coding:utf-8

'''
用法：re.search( pattern, string )
使用最為頻繁、且最容易使用
pattern: 資料型式
string: 要比對的文字
'''

'''
re.match()
從頭開始比對文字
與re.search()的最大差別在於它是檢測文字是否在開頭位置。
用法：re.match( pattern, string )
'''

'''
re.findall()
找尋文字中所有匹配的文字
'''

# Python中的re.search和re.group用法
'''
re.search()方法扫描整个字符串，并返回第一个成功的匹配。如果匹配失败，则返回None。

与re.match()方法不同，re.match()方法要求必须从字符串的开头进行匹配，如果字符串的开头不匹配，整个匹配就失败了；

re.search()并不要求必须从字符串的开头进行匹配，也就是说，正则表达式可以是字符串的一部分。
'''
# group（）用来提出分组截获的字符串吗，（）用来分组
# group() 同group（0）就是匹配正则表达式整体结果。
# group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。
# 当正则表达式中没有括号，group(1)是有误的。

'''
【m.group()】(這裏m是search或者match後生成的對象)
<傳入N>0>
返回第N組括號匹配的字符。（正則表達式內有幾個()就有幾個分組）
'''

'''
【m.groups()】
m.groups() 返回所有括號匹配的字符（正則表達式中有幾個括號就會有幾個分組的字符串內容展示），以tuple格式作為容器返回。
'''
import re

# 当一个字符串使用了正则表达式后，最好在前面加上r，避免多次转义造成的反斜杠困扰，不用担心漏写反斜杠，写出来的表达式也更直观。
s = '\\100'
ret_1 = re.match('\\\\1', s)
ret_2 = re.match(r'\\1', s)

# 1、匹配1-100之间的数
s = '100'
print(re.search('100|[1-9]{1,2}', s).group())

# 2、匹配座机号码
# 010-12345678，其构造规则为[3位数字][-][8位数字]；或者0431-1234567，其构造规则为[4位数字] [-][7位数字]
s_0 = '010-12345678'
print(re.findall('\d{3}-\d{8}', s_0))


# 3、匹配5-10位纯数字组成的qq号码，且不能以0开头
s = "11010"
print(re.match(r'[1-9]\d{4,9}', s).group(0))

# 4、取出字符串中的所有字母
s1 = "43arwer32656fafa6546jjuy#H"
print(re.search(r'43(\w{5})32656(.*)6546(\w+)#(.+)', s1).groups())
print(re.findall(r'[a-zA-Z]+', s1))

# 5、找出以字母y结尾的单词，忽略大小写
s2 = 'study hard and make progress every day'
res = re.compile(r'\w+y\b', re.I)
print(res.findall(s2))
'''
r'\w+y\b'的匹配规则
字母“y”前面的有1个或多个字符（\w+）
单词的边界线(\b) -即单词与空格间的位置
匹配到了以y结尾的单词以及\b匹配到单词的边界线，以上单词中以y结尾的单词有：'study', 'every', 'day'
'''

# 6、将多个重复的字母替换成&
s3 = "PythondddJavauuuHTMLFFPHP"
res = re.compile(r'([a-zA-Z])\1+')
ret = res.sub('&', s3)

test = re.sub(r'([a-zA-Z])\1+', '&', s3)  # 相當於如果監測到有大寫or小寫字母重複多次則提取, 替換成'&'; 替換目標為s3
print(ret)
print(test)
'''
\1+表示重复匹配正则中第一个圆括号内匹配到的内容，则匹配到了'ddd', 'uuu', 'FF'，就是将([a-zA-Z])匹配到的内容匹配多次
res.sub('&', s)是将正则表达式匹配到的内容替换为'&'
参数：re.sub(pattern, repl, string, count=0, flags=0) 

pattern : 正则中的模式字符串。

repl : 替换的字符串，也可为一个函数。

string : 要被查找替换的原始字符串。

count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
'''

# 7、将字符串变成 '我要学Python编程’
s4 = "我我...我我...我要..要要...要要...学学学...学学..Python...编编编..编程..程.程...程...程"
ret = re.sub('\W+', '', s4)  # 提取非數字字符下划線的內容, 即去掉..符號
print(ret)
res_ = re.sub(r'(.)\1+', r'\1', ret)
'''
1、'.'可以匹配除换行符 \n 之外的任何单字符；
2、'(.)\1+'：使用括号(.)代表为组第一次出现则为第一组，\1引用的是第一个括号（分组）中匹配成功后的内容，
r'(.)\1+'将第一组中"."匹配的内容匹配多次（如：“我我我我我”），r'\1'将第一组中匹配的内容匹配一次（如：“我”）；
3、re.sub(r'(.)\1+',r'\1',res)：将r'(.)\1+'匹配到的内容（如：“我我我我我”）替换为r'\1'（如：“我”）
'''
print(res_)

# Match	cat.
# Match	896.
# Match	?=+.
# Skip	abc1

# Ans: regl = ...\.

# Match	aaaabcc
# Match	aabbbbc
# Match	aacc
# Skip	a

# Ans: regl = aa+b*c+ | a{2,4}b{0,4}c{1,2}


# ？（問號）表示可選性的元字符。此元字符允許您匹配零個或前面的字符或組之一。例如，模式ab?c將匹配字符串“abc”或“ac”，因為 b 被認為是可選的。

# Match	1 file found?
# Match	2 files found?
# Match	24 files found?
# Skip	No files found.

# regl = \d+ files? found\?

# Difference between \n and \r?  In terms of ascii code, it's 3 -- since they're 10 and 13 respectively
# \n is the code for end-of-line, \r means nothing special


# 特殊字符\s將匹配上面的任何特定空格，並且在處理原始輸入文本時非常有用。 \n\r\t''

# Match	1.   abc
# Match	2.	abc
# Match	3.           abc
# Skip	4.abc

# regl = \d.\s+abc


# ^ ( hat ) 和$ (美元符號) --行的開頭和結尾, ^success僅匹配以單詞“success”開頭的行
# 這與一組括號[^...]中用於排除字符不同

# Match	Mission: successful
# Skip	Last Mission: unsuccessful
# Skip	Next Mission: successful upon capture of target

# regl = ^Mission: successful$


# () -and;  | -or
# ^(IMG\d+\.png)$ -捕獲和提取完整的文件名;  ^(IMG\d+) \.png$僅捕獲句點之前的部分

# Capture	file_record_transcript.pdf	//Capture Groups: file_record_transcript
# Capture	file_07241999.pdf	//Capture Groups: file_07241999
# Skip	testfile_fake.pdf.tmp

# regl = (^file.+)\.pdf$


# multiple layers of information -> nested groups
# nested group在模式中從左到右讀取，第一個捕獲組是第一個括號組的內容，依此類推
# 如果每個圖像文件的文件名中有一個連續的圖片編號，您可以使用相同的模式提取文件名和圖片編號 -> ^(IMG(\d+))\.png$

# Capture	Jan 1987	//Capture Groups: Jan 1987 1987
# Capture	May 1969	//Capture Groups: May 1969 1969
# Capture	Aug 2011	//Capture Groups: Aug 2011 2011

# regl = ([A-Z].+(\d{4}))  or  (\w+ (\d+))



# Task		Text       Capture Groups
# Capture	1280x720	1280 720
# Capture	1920x1600	1920 1600
# Capture	1024x768	1024 768

# regl = (\d+)x(\d+)


# .* because you would have no idea what you could get back.
# we can actually define these conditionals explicitly. -- a|b|c

# for example, ([cb]ats*|[dh]ogs?) --  cats or bats, or, dogs or hogs

# Match	I love cats
# Match	I love dogs
# Skip	I love logs
# Skip	I love cogs

# regl = I love (cats|dogs)


# \D -非數字,  \S -非空白,  \W -非字母數字字符（例如標點符號）
# \b -匹配單詞和非單詞字符之間的邊界。它在捕獲整個單詞時最有用（例如通過使用模式\w+\b）

# 反向引用 -\0（通常是完整匹配的文本）,  \1（第 1 組）,  \2 （第 2 組）
# "\2-\1" 以將第二個捕獲的數字放在首位


# Match	The quick brown fox jumps over the lazy dog.
# Match	There were 614 instances of students getting 90.0% or above.
# Match	The FCC had to censor the network for saying &$#*@!.

# regl = .*

import re

s = 'study hard and make progress every dai'
# 从study匹配，匹配study后匹配到边界线，hard and make progress不满足匹配条件
# every和day满足字母“y”前面的有1个或多个字符（\w+），而“y”后面是单词的边界线匹配条件
res = re.compile(r'\w+y\b', re.I)  # \b为边界
ret = res.findall(s)
print(ret)
# '\w+y$'可以匹配以y字母结尾，但\w+无法匹配day前到空格，所以最终匹配结果是'day'
res = re.compile(r'\w+y$', re.I)  # $匹配以某一字符结尾
ret = res.findall(s)
print(ret)



