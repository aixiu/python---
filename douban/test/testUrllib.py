#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE
import re
from urllib import response
import urllib.request

# 获取一个 get 请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8')) # 对获取到的网页源码进行 utf-8解码

# 获取一个 post 请求
# 第一种写法
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(response.read().decode("utf-8"))

# 第二种写法
# qu_string = {"hello": "world"}
# data = urllib.parse.urlencode(qu_string).encode("utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(response.read().decode("utf-8"))


# 超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")


# 获取响应头信息
# response = urllib.request.urlopen("http://httpbin.org/get")
# print(response.status)  # 查看状态码
# print(response.getheaders())  #查看所有 headers 信息
# print(response.getheader("Date"))  # 查看一个属性值 去掉 getheaders 的 s


# 引用伪装 headers 头
# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
# }
# data = urllib.parse.urlencode({"name": "eric"}).encode("utf-8")
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


url = "https://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
