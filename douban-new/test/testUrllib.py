# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/11/05 18:11:33

import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
print(response)