# coding:utf-8

import xlsxwriter  # pip install xlsxwriter
import xlrd

# excel = xlsxwriter.Workbook('write.xlsx')  --> excel_obj
# book = excel.add_worksheet('study')  --> worksheet_obj
#
# title = ['姓名', '性别', '年龄', '成绩', '等级']
#
# for index, data in enumerate(title):
#     book.write(0, index, data)
# excel.close()

def read():
    result = []  # 用大列表包含每列的內容
    excel = xlrd.open_workbook('study.xlsx')  # 讀取excel_obj
    book = excel.sheet_by_name('学生手册')  # 獲取工作簿 -按照名稱獲取
    for i in book.get_rows():
        content = []
        for j in i:
            content.append(j.value)
        result.append(content)
    return result


def write(content):
    excel = xlsxwriter.Workbook('write.xlsx')
    book = excel.add_worksheet('study')

    for index, data in enumerate(content):
        print(data)  # 依據 index 列數打印
        for sub_index, sub_data in enumerate(data):  # 寫內容: sheet.write(rows_index, cols_index, content)
            #  index列數, sub_index為第幾列的第幾行
            book.write(index, sub_index, sub_data)

    # 重頭寫一個新的工作簿
    book1 = excel.add_worksheet('学生等级')  # 創建work_sheet工作簿
    data = [
        ['优秀', '良好', '中', '差'],
        [1100, 2000, 1000, 900]
    ]

    book1.write_column('A1', data[0])  # 按行添加 -A1這直行 data[0]
    book1.write_column('B1', data[1])  # 按行添加 -B1這直行 data[1]

    # 圖表製作
    chart = excel.add_chart({'type': 'pie'})  # 創建圖表對象, 定義圖表類型 -type: 柱狀圖

    # 數據 -categories標題, values數據, name表名
    chart.add_series({
        'categories': '=学生等级!$A1:$A4',
        'values': '=学生等级!$B1:$B4',
        'name': '成绩占比'  # 定義數據名稱
    })
    chart.set_title({'name': '成绩占比图表'})  # 定義圖表名稱
    book1.insert_chart('A10', chart)  # 添加圖表進入工作簿

    excel.close()  # 保存資料


if __name__ == '__main__':
    result = read()
    print(result)
    write(result)

