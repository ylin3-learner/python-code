# coding: utf-8

# else 就是 if 條件不滿足執行另一個代碼塊的入口

"""
if bool_result:
    do
 else:
    elsedo
"""

url = 'https://www.imooc.com'

if 'www.imooc.com' in url:
    print('已進入慕課網的世界, 請好好學習!')
else:
    print('請前往慕課網學習python')

if 'www.imooc.com' in url:
    _url = 'www.imooc.com'
else:
    _url = None
print('url is %s' % _url)


