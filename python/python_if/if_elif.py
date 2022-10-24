# coding: utf-8

# elif(或者如果)對於命題的非第一次的多種判斷, 每一種對應一組業務代碼
# 對於首次if判斷不滿足後, 其他條件的判斷語句
'''
 if bool_result:
    do
 elif bool_result:
    elif do
 else:
    else do
'''

# 條件與滿足一個條件後, 將退出當前條件語句

number = 20

if number > 10:
    print('number\'s value is larger than 10.')
elif 5 < number <= 10:
    print('number\'s value is between 5 and 10.')
elif 0 < number <= 5:
    print('number\'s value is 1~5.')
else:
    print('number\'s value is 0 or a negative number.')

print('finishied')


user = [
    ('dewei', 33, 90),
    ('xiaomu', 10, 99),
    ('xiaoming', 18, 100)
]

xiaoming = ['xiaomings', 19, 90]

if user[0][0] == xiaoming[0]:
    xiaoming[0] = '%s_new' % xiaoming[0]
    user.append(xiaoming)
elif user[1][0] == xiaoming[0]:
    xiaoming[0] = '%s_new' % xiaoming[0]
    user.append(xiaoming)
elif user[2][0] == xiaoming[0]:
    xiaoming[0] = '%s_new' % xiaoming[0]
    user.append(xiaoming)
else:
    user.append(xiaoming)

print(user)


users ={
    'dewei': {'age': 33, 'count': 99},
    'xiaomu': {'age': 10, 'count': 99},
    'xiaoming': {'age': 18, 'count': 100}
}

if xiaoming[0] in users:
    xiaoming[0] = '%s_new' % xiaoming[0]
else:
    users[xiaoming[0]] = {'age': xiaoming[1], 'count': xiaoming[2]}
print(users)
