# coding:utf-8

d = {'lin': '123456'} # 資料庫字典, 所有使用者的名稱、密碼存於此

count = 5  # 還有幾次輸入密碼的機會
while count:# 如果出現錯誤的話，可以繼續迴圈。
    name = input('請輸入使用者名稱:')
    if name in d:
        break

    else:
        count -= 1
        print('使用者名稱不正確, 還有{}次輸入機會!'.format(count))
        continue

while count:
    password = input('請輸入使用者密碼:')
    if d.values() == password:
        print('進入系統!')
        break
    else:
        count -= 1
        print('密碼不正確!還有%d次輸入機會' % count)
        continue