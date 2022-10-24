# coding: utf-8

none_list = [None, None, None]

print(none_list)
print(bool(none_list))
print(len(none_list))
print([])
print(bool([]))

max_list = ['1',"youlun",'None', '3.14', '[1, 2, 3.14]']

print(max(max_list))
print(min(max_list))
print(id(max_list))

id_address = id(max_list)

print(id_address)