#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

import xlwt


'''
workbook = xlwt.Workbook(encoding="utf-8")  # 创建workkkbkook 对象 相当于一个excel文件
worksheet = workbook.add_sheet("sheet1")  # 相当于在 excel 文件中创建一个表
worksheet.write(0, 0, "hello")   # 写入数据，第一个参数为行，第二个参数为列，第三个参数为内容
workbook.save('student.xls')
'''

workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook 对象 相当于一个excel文件
worksheet = workbook.add_sheet("sheet1")  # 相当于在 excel 文件中创建一个表
for i in range(0, 9):
    for j in range(0, i+1):
        worksheet.write(i, j, "{}*{}={}".format(i+1, j+1, (i+1)*(j+1)))

workbook.save('student.xls')