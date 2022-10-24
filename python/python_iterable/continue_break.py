# coding: utf-8

# 循環遇到 continue 將停止本次數據循環, 進入下一次循環
'''
count = 1
while count < 5:
    print(count)
    continue
    count += 1
'''

# break 使循環停止不報錯, 如果配合else, 則else不執行
'''
count = 1         
while count < 5:     在while循環中, 對break優先於while的判斷
    print(count)
    count += 1
>>> 1
'''

# coding: utf-8

users = [
    {'username': 'dewei', 'age': 33, 'top': 174, 'sex': 'man'},
    {'username': 'xiaomu', 'age': 10, 'top': 175, 'sex': 'man'},
    {'username': 'xiaoyun', 'age': 18, 'top': 165, 'sex': 'woman'},
    {'username': 'xiaogao', 'age': 18, 'top': 174, 'sex': 'man'}
]

man = []
for user in users:
    if user.get('sex') == 'woman':
        continue  # 當進入到if循環體內, xiaoyun為女, 但遇到continue, 因此結束這次循環後兩句也沒有執行
    man.append(user)
    print('%s 加入了幫忙的行列' % user.get('username'))
print(man)


l = range(100)

for i in l:
    if i == 80:
        print('----')
        print('已經循環80次了, 程序要退出了!')
        # break
    print(i)
else:
    print('程序正常退出了')

