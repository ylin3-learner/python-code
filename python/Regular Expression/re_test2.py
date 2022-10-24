# coding:utf-8

# 判斷是否為合法的網址

import re


url = 'https://www.imooc.com/'

def check_url(url):
    result = re.findall('[a-zA-Z]{4,5}://\w*\.*\w+\.\w+', url)  # findall() -return all the matches of the string
    # [字母大小寫都可]{長度4-5}://, \w+ -有可能為數字:1次-多次, \.轉義字符
    return len(result) != 0


def get_url(url):
    result = re.findall('https://(\w*\.*\w+\.\w+)', url)  # 如果只想要字符串中某一部分, 通過組個概念拿出
    if len(result) != 0:
        return result[0]  # 由於組的值只有一個, 返回0
    else:
        return ''


def get_email(email):
    # result = re.findall('[0-9A-Za-z]+@[0-9a-zA-Z]+\.[a-zA-Z]+', email)  # findall() -return all the matches of the string
    result_2 = re.findall(r'.+@.+\.[a-zA-Z]+', email)  # 使用通配符 -可以獲取到所有信息, 包括組以外
    return result_2  # 如果沒有, 則返回空列表
    # 可以是字母,數字,字符, 且匹配多個[0-9a-zA-Z]+


html = ('<div class="s-top-nav", style="display:none:">'  # 希望獲取style="display:none:"
        '</div><div class="s-center-box"></div>')

def get_html_data(html):
    result = re.findall('style="(.*?)"', html)  # * -貪婪模式, 會一直往後找 "" - ? 不貪婪
    return result

def get_all_html_data(data):
    result = re.findall('="(.+?)"', html)
    return result

if __name__ == '__main__':
    result = check_url(url='http://baidu.com/')
    print(result)
    result = get_url(url='https://www.baidu.com/')
    print(result)
    result = get_email(email='dewei@imooc.net')
    print(result)

    result = get_html_data(html=html)
    print(result)

    result = get_all_html_data(data=html)
    print(result)

