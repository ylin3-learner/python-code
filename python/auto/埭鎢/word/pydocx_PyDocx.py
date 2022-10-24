# coding:utf-8

# word [f = open('.html', 'w', encoding='utf-8')]==> html -[pdfkit.from_file]==> pdf

# word -> html -pydocx
'''
pip install pydocx,  from pydocx import PyDocx, html = PyDocx.to_html(word.docx)
f = open('.html', 'w')
'''
import pdfkit
from pydocx import PyDocX  # pip install pydocx

html = PyDocX.to_html('簡歷1.docx')  # 將word.docx轉化為html_str
f = open('html1.html', 'w', encoding='utf-8')
f.write(html)
f.close()

# 在 Python 代码里面添加手动添加 wkhtmltopdf 的路径即可

# 设置 wkhtmltopdf 路径
path_wk = r'C:\Users\user\Desktop\wkhtmltox\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wk)
# pdfkit.from_file('html1.html', 'test3.pdf', configuration=config)  # html -> pdf  --from_file(html_file, save_path)

# 使用 wkhtmltopdf 路径输出 PDF
pdfkit.from_string(html, 'test3.pdf', config)

pdfkit.from_url(r'https://ucan.moe.edu.tw/service/file_1.aspx', 'personal_test.pdf', config)

