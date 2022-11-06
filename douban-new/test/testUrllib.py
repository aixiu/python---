# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/11/05 18:11:33

import urllib.request

# 获取一个 get 请求
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))  # 对获取到的网页源码进行 utf-8解码

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
try:
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("time out!")