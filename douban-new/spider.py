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
    # saveData(savepath)
    
    askURL('https://movie.douban.com/top250?start=')
    

# 爬取网页    
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数，10次
        url = baseurl.format(str(i * 25))
        html = askURL(url)  # 保存获取到的网页源码
        
        # 2.逐一解析数据

    
    
    
    
    return datalist

# 得到指定一个 URL 的网页内容
def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
    }
    # 用户代理，表示，告诉豆瓣服务器，是什么类型的机器。
    # 模拟浏览器头部信息，向 豆瓣服务器发送信息
    request = urllib.request.Request(url=url, headers=headers)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):   # hasattr() 函数用于判断对象是否包含对应的属性。
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
            
    return html
    
# 保存数据
def saveData(savepath):
    print('save....')
    
if __name__ == '__main__':
    # 调用函数
    main()