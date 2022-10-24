# coding:utf-8

# word -> html
# html -> pdf
from pydocx import PyDocX
import pdfkit

html = PyDocX.to_html('coding_review.docx')

f = open('test_word.html', 'w', encoding='utf-8')
f.write(html)
f.close()

# html -> pdf
path_wk = r'C:\Users\user\Desktop\wkhtmltox\bin\wkhtmltopdf.exe'  # abs_route
config = pdfkit.configuration(wkhtmltopdf=path_wk)  # 系統授權

pdfkit.from_string(html, 'save_test_word.pdf', configuration=config)