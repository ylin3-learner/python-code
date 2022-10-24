# coding: utf-8

user_info = {'name': "youlun", 'age': 19, 'height': '170cm'}

result = 'name' in user_info
print(result)

result_2 = 'hope' in user_info
print(result_2)

result_3 = 'hope' not in user_info
print(result_3)

count = len(user_info)
print(count)
print(bool(user_info))
print(type(user_info))

empty_dict = {}
print(bool(empty_dict))
print(type(empty_dict))
print(type(dict(empty_dict)))

print(max(user_info))
print(min(user_info))
