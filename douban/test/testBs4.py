#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

"""
BeautifulSoup4将复杂 HTML 文档转换成一个复杂的树形结构，每个节点都是 python 对象，所有对象可以归纳为 4 种：

- Tag
- NavigableString
- BeautifulSoup
- Comment
"""

from bs4 import BeautifulSoup

file = open("./baidu.html", mode="rb")
html = file.read()

bs = BeautifulSoup(html, "html.parser")   # html.parser是Python内置的专门用来解析HTML的模块

# 1.Tag 标签及其内容：拿到它所找到的第一个内容
# print(bs.title)
# print(bs.a)
# print(bs.head)
# print(type(bs.head))   # <class 'bs4.element.Tag'>


# 2.NavigableString 标签里的内容（字符串）
# print(bs.title.string)
# print(type(bs.title.string))  # <class 'bs4.element.NavigableString'>


# 3.标签里的属性（字典）
# print(bs.a.attrs)
# print(bs.a.attrs["href"])


# 4.BeautifulSoup  表示整个文档
# print(bs.name)
# print(bs.attrs)
# print(bs)

# 5.Comment 是一个特殊的NavigableString，输出的内容不包含注释符号
# print(bs.a.string)
# print(type(bs.a.string))  # <class 'bs4.element.Comment'>


# --------------------------------------

# 文档的遍历  
# contents: 获取Tag的所有子节点，返回一个 list

# print(bs.head.contents)
# print(bs.head.contents[1])

# children: 获取Tag的所有子节点，返回一个 生成器

# for child in bs.body.children:
#     print(child)

# 文档的搜索

# 1.find_all() 字符串过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")

import re
# 2.正则表达式搜索 使用 search() 方法来匹配内容
# t_list = bs.find_all(re.compile("a"))


# 方法： 传入一个函数（方法），根据函数的要求来搜索  （了解）
# def name_is_exists(tag):
#     return tag.has_arrt("name")   # 判断标签是否有响应属性  判断给定标签有没有 name 属性

# t_list = bs.find_all(name_is_exists)
# print(t_list)


# 3.参数

# t_list = bs.find_all(id="head")

# t_list = bs.find_all(class_=True)   
# 查询所有包含class的Tag(注意：class在Python中属于关键字，所以加_以示区别)

# t_list = bs.find_all(href="http://news.baidu.com")

# for item in t_list:
#     print(item)

# 4.text 参数

# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123", "地图", "贴吧"])

# t_list = bs.find_all(text=re.compile("\d"))   # 应用正则表达式来查找包含特定文本的内容（标签里的字符串）


# 5.limit 参数

# t_list = bs.find_all("a", limit=3)

# for item in t_list:
#     print(item)

# css选择器
# t_list = bs.select("title")  # 通过标签来查找

# t_list = bs.select(".mnav")  # 通过类名 class 查找

# t_list = bs.select("#u1")  # 通过 ID 来查找

# t_list = bs.select("a[class='bri']")  # 通过属性来查找  a标签里带 bri属性的

# t_list = bs.select("head > title")  # 通过子标签来查找

# for item in t_list:
#     print(item)


t_list = bs.select(".mnav ~ .bri")
print(t_list[0].get_text())

