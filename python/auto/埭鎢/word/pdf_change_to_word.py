# coding: utf-8
import PyPDF2
import pdfplumber
import os

# PyPDF2, pdfplumber这两个库不属于python标准库，都需要单独安装；
path = r'C:\Users\user\Desktop\python\auto\埭鎢\word\taken_courses.pdf'
with pdfplumber.open(path) as p:
    page = p.pages[0]
    print(page.extract_text())