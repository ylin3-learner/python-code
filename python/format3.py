# coding: utf-8

info_n = ('my name \nis %s\n' % 'youlun')
print(info_n)

info_tt = ('my name \tis %s\n' % 'youlun')
print(info_tt)
info_t = ('my name\tis %s\n' % 'youlun')
print(info_t)

info_v = 'my name \vis youlun'
print(info_v)

info_a = 'my name \ais youlun'
print(info_a)

info_b = 'my name is youlun\b'
print(info_b)

info_r = 'my name is youlun\r'
print(1, info_r + '....')  # \r 會把它之前的所有信息前全部抹去再換行

info_f = 'my name is youlun\f'
print(info_f)

print('my name is \'youlun\'')
print('my name is \"youlun\"')
print('my name is \\ youlun')

print(r'my name is \\ youlun\n')

print(r'my name is %s ' % 'youlun')
