# coding: utf-8

info = 'This is a string example!!'

res = info.startswith('This')
res_2 = info.endswith('my')

print(res)
print(res_2)

result = info.startswith('This is a string example!!')
print(result)

print(bool(info == 'This is a string example!!' ))

print('result_2:', bool(info.endswith('!')))

