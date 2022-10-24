# coding:utf-8

import xlrd

excel = xlrd.open_workbook('study.xlsx')  # excel_obj

book = excel.sheet_by_name('学生手册')  # worksheet_obj
print(book)

book = excel.sheet_by_index(0)
print(book.name)

for i in excel.sheets():
    print(i.name)

print(book.nrows)  # 總列數
print(book.ncols)  # 總行數


for i in book.get_rows():  # 循環每列
    # i 為text是一個對象
    content = []
    # i == [text:'姓名', text:'性别', text:'年龄', text:'成绩', text:'等级']
    for j in i:  # 循環每列內容中具體的對象
        # j == text:'姓名', text:'性别', text:'年龄', text:'成绩', text:'等级'
        content.append(j.value)  # 獲取text中的值 j.value
    print(content)


'''
for i in book.get_rows():
    print(i)
    for j in i:
        print(j)
'''

