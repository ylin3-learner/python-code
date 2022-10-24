# coding:utf-8

# pdf 工具包(pdfkit) - word -> html -> pdf
# pdfkit - pip install htmltopdf
# https://wkhtmltopdf.org/downloads.html -> 下載符合操作系統的軟體

# import pdfkit – pip install htmltopdf
# html -> pdf :  pdfkit.from_file(html, save_pdf_path)
# str/html -> pdf: pdfkit.from_string(html based str, save_pdf_path)
# url -> pdf: pdfkit.from_url(url, save_pdf_path)


import pdfkit

html = ''' 
<html>
<head>
</head>
<meta charset="utf-8" />
<body>
    <p>你好</p>
</body>
</html>
'''

# /...表示結尾的意思

if __name__ == '__main__':
    # 找到wkhtmltopdf.exe的安裝絕對路徑位置
    # 且因為版本不兼容的關係, 需要授權
    path_wk = r'C:\Users\user\Desktop\wkhtmltox\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wk)
    pdfkit.from_url(r'https://www.imooc.com', 'test1.pdf', configuration=config)
    pdfkit.from_string(html, 'test2.pdf', configuration=config)
    # pdfkit.from_url(r'https://ucan.moe.edu.tw/service/file_1.aspx', 'personal_test.pdf', config)




