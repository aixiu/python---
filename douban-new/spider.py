# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/11/03 11:38:12

# 视频地址：https://www.bilibili.com/video/BV12E411A7ZQ/?p=16&vd_source=20f7c1f5f32f90ae92d9428e45039d9b

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行 excel 文件写入操作   Excel的写插件  安装命令：pip install xlwt；  Excel的读取插件  安装命令：pip install xlrd
import sqlite3  #  进行SQLite数据库操作

'''
Python 字符串前加f,r,u,b的含义

1. 字符串前加f
表示字符串内支持大括号内的python表达式，如：
logger.info(f"Total time taken: {time.time() - start_time}")

2. 字符串前加r
去掉反斜杠的转移机制，如下面例子，表示单纯字符串而不表示换行
logger.info(r"Test\n\n\n")

3. 字符串前加u
一般出现在中文字符串前，防止出现乱码

4. 字符串前加b
表示这是一个bytes类型对象，在网络编程中，服务器和浏览器只认bytes类型数据，如：
response=b'<h1>Hello World</h1>'

'''

def main():
    baseurl = "https://movie.douban.com/top250?start={}"  # 基础 URL
    # 1.爬取网页
    datalist = getData(baseurl)    
    
    savepath = r'./豆瓣电影Top250.xls'
    # 3.保存数据
    saveData(savepath)
    

# 爬取网页    
def getData(baseurl):
    datalist = []
    # 2.逐一解析数据
    return datalist
    
# 保存数据
def saveData(savepath):
    print('save....')
    
if __name__ == '__main__':
    # 调用函数
    main()
