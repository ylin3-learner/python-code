# coding: utf-8

info = '   my name is youlun    '
new_info = info.strip()

print('.' + new_info + '.')

info_01 = new_info.strip(new_info)
print('.' + info_01 + '.')
print(len(info_01))

new_str = 'abcdea'
print(new_str.strip('a'))
print(new_str.lstrip('a'))
print(new_str.rstrip('a'))




