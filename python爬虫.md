# Python爬虫

## 1.任务介绍

- 需求分析

爬取豆瓣电影Top250的基本信息，包括电影的名称，豆瓣评分，评价数，电影概况，电影链接等。

<https://movie.douban.com/top250>

## 2.爬虫初识

- 什么是爬虫
  - 网络爬虫,是- -种按照一定规则，自动抓取互联网信息的程序或者脚本。由于互联网数据的多样性和资源的有限性,根据用户需求定向抓取相关网页并分析已成为如今主流的爬取策略。
- 爬虫可以做什么
  - 你可以爬取妹子的图片,爬取自己想看的视频等等,只要你能通过浏览器访问的数据都可以通过爬虫获取。
- 爬虫的本质是什么
  - 模拟浏览器打开网页,获取网页中我们想要的那部分数据。

## 3.基本流程

- 准备工作
  - 通过浏览器查看分析目标网页 ,学习编程基础规范。
- 获取数据
  - 通过HTTP库向目标站点发起请求,请求可以包含额外的header等信息,如果服务器能正常响应,会得到一-个Response ,便是所要获取的页面内容。
- 解析内容
  - 得到的内容可能是HTML、json等格式,可以用页面解析库、正则表达式等进行解析。
- 保存数据
  - 保存形式多样,可以存为文本,也可以保存到数据库,或者保存特定格式的文件。

### 3.1准备工作

- URL分析
  - 页面包括250条电影数据，分10页，每页25条
  - 每页的URL不同之处：最后的数据 = （页数-1）*25

#### 3.1.1页面分析

借助Chrome开发者工具( F12 )来分析网页,在Elements下找到需要的数据位置

####  3.1.2编码规范

- 般Python程序第一-行需要加入

```python
 # -*- coding: utf-8 -*- 或者# coding=utf-8
```

这样可以在代码中包含中文

- 在Python中,使用函数实现单一功能或相关联功能的代码段，可以提高可读性和代码重复利用率,函数代码块以def关键词开头,后接空格、函数标识符名称、圆括号()、冒号: ,括号中可以传入参数，函数段缩进( Tab或四个空格,只能任选-种) , `return`用于结束函数，可以返回一个值,也可以不带任何表达式(表示返回None )
- Python文件中可以加入main函数用于测试程序
  `if __name__ == '__main__':`
- Python使用#添加注释,说明代码(段)的作用

####  3.1.3引入模块

模块( module ) :用来从逻辑上组织Python代码(变量、函数、类) , 本质就是py文件,提高代码的可维护性。Python使用import来导入模块 ,如 *import sys*

### 3.2获取数据

- python一般使用urllib库获取面页

- 获取页面数据

  - 对每一个页面，获取面面内容

  - 定义一个获取页面函数，传入一个url参数，表示网址，如：<https://movie.douban.com/top250?start=0>

  - *urllib.request*生成请求，*urllib.urlopen*发送请求获取响应，*read*获取页面内容

  - 在访问页面时经常会出现错误，为了程序正常运行，加入异常捕获 *try...except...*语句

#### 补充：urllib模块

- 最最基本的请求

- 这是python内置的一个http请求库，不需要额外的安装。只需要关注请求的链接，参数，提供了强大的解析。

  - urllib.request 请求模块
  - urllib.error 异常处理模块
  - urllib.parse 解析模块

- 用法讲解

  - 简单的一个get请求

  - ```python
      import urllib.request
      reponse = urllib.request.urlopen('http://baidu.com')
      print(reponse.read().decode('utf-8'))
      ```

### 3.3解析内容

- 解析页面内容
  - 使用*BeautifulSoup*定位特定的村签位置
  - 使用正则表达式找到具体的内容

#### 3.3.1标签解析

- Beautiful Soup

Beautiful Soup是一个库,提供一些简单的、 `python`式的用来处理导航、搜索、修改分析树等功能,通过解析文档为用户提供需要抓取的数据。我们需要的每个电影都在一个<div> 的标签中, 且每个`div`标签都有一个属性`class= "item'`。

#### 补充：BeautifulSoup模块

参考： http://www.jsphp.net/python/show-24-214-1.html
**1.BeautifulSoup4简介**
BeautifulSoup4和 lxml 一样，Beautiful Soup 也是一个HTML/XML的解析器，主要的功能也是如何解析和提取 HTML/XML 数据。

BeautifulSoup支持Python标准库中的HTML解析器,还支持一些第三方的解析器，如果我们不安装它，则 Python 会使用 Python默认的解析器，lxml 解析器更加强大，速度更快，推荐使用lxml 解析器。

Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅
仅需要说明一下原始编码方式就可以了。

**2.BeautifulSoup4主要解析器，以及优缺点：**

下表列出了主要的解析器，以及它们的优缺点，官网推荐使用lxml作为解析器，因为效率更高。在Python2.7.3之前的版本和Python3中3.2.2之前的版本，必须安装lxml或html5lib，因为那些Python版本的标准库中内置的HTML解析方法不够稳定。

|      解析器      |                           使用方法                           |                          优势                           | 劣势                                            |
| :--------------: | :----------------------------------------------------------: | :-----------------------------------------------------: | ----------------------------------------------- |
|   Python标准库   |            `BeautifulSoup(markup, "html.parser")`            |     Python的内置标准库 执行速度适中 文档容错能力强      | Python 2.7.3 or 3.2.2)前 的版本中文档容错能力差 |
| lxml HTML 解析器 |               `BeautifulSoup(markup, "lxml")`                |                  速度快 文档容错能力强                  | 需要安装C语言库                                 |
| lxml XML 解析器  | `BeautifulSoup(markup, ["lxml", "xml"])BeautifulSoup(markup, "xml")` |               速度快 唯一支持XML的解析器                | 需要安装C语言库                                 |
|     html5lib     |             `BeautifulSoup(markup, "html5lib")`              | 最好的容错性 以浏览器的方式解析文档 生成HTML5格式的文档 | 速度慢 不依赖外部扩展                           |

**3.BeautifulSoup4简单使用**
假设有这样一个Html，具体内容如下：

```html
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta content="always" name="referrer">
    <link rel="stylesheet" href="https://pss.bdstatic.com/r/www/cache/static/protocol/https/soutu/css/soutu_new2_dd3a84f.css" type="text/css" rel="stylesheet">       
    <title>百度一下，你就知道</title>
</head>
<body link="#0000cc">
    <div id="wrapper">
        <div id="head">
            <div class="head_wrapper">
                <div id="u1">
                    <a class="mnav" href="http://news.baidu.com" name="tj_trnews"><!--新闻--></a> 
                    <a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻</a>
                    <a class="mnav" href="https://www.hao123.com" name="tj_hao123">hao123</a>
                    <a class="mnav" href="http://map.baidu.com" name="tj_trmap">地图</a>
                    <a class="mnav" href="https://v.baidu.com" name="tj_trvideo">视频</a>
                    <a class="mnav" href="http://tieba.baidu.com" name="tj_trtieba">贴吧</a>
                    <a class="bri" href="http://www.baidu.com/more/" name="tj_triicon">更多产品</a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

**创建beautifulsoup4对象：**

```python
from bs4 import BeautifulSoup
file = open('./aa.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser") # 缩进格式
print(bs.prettify()) # 获取title标签的所有内容
print(bs.title) # 获取title标签的名称
print(bs.title.name) # 获取title标签的文本内容
print(bs.title.string) # 获取head标签的所有内容
print(bs.head) # 获取第一个div标签中的所有内容
print(bs.div) # 获取第一个div标签的id的值
print(bs.div["id"]) # 获取第一个a标签中的所有内容
print(bs.a) # 获取所有的a标签中的所有内容
print(bs.find_all("a")) # 获取id="u1"
print(bs.find(id="u1")) # 获取所有的a标签，并遍历打印a标签中的href的值
	for item in bs.find_all("a"):
print(item.get("href")) # 获取所有的a标签，并遍历打印a标签的文本值
	for item in bs.find_all("a"):
print(item.get_text())
```



**4.BeautifulSoup4四大对象种类**
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以
归纳为4种:

- Tag
- NavigableString
- BeautifulSoup
- Comment

**（1）Tag**

Tag通俗点讲就是HTML中的一个个标签，例如：

```python
from bs4 import BeautifulSoup
file = open('./aa.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser")
# 获取title标签的所有内容
print(bs.title)
# 获取head标签的所有内容
print(bs.head)
# 获取第一个a标签的所有内容
print(bs.a)
# 类型
print(type(bs.a))
```

我们可以利用 soup 加标签名轻松地获取这些标签的内容，这些对象的类型是bs4.element.Tag。但是
注意，它查找的是在所有内容中的第一个符合要求的标签。
对于 Tag，它有两个重要的属性，是 name 和 attrs：

```python
from bs4 import BeautifulSoup
file = open('./aa.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser")
# [document] #bs 对象本身比较特殊，它的 name 即为 [document]
print(bs.name)
# head #对于其他内部标签，输出的值便为标签本身的名称
print(bs.head.name)
# 在这里，我们把 a 标签的所有属性打印输出了出来，得到的类型是一个字典。
print(bs.a.attrs)
#还可以利用get方法，传入属性的名称，二者是等价的
print(bs.a['class']) # 等价 bs.a.get('class')
# 可以对这些属性和内容等等进行修改
bs.a['class'] = "newClass"
print(bs.a)
# 还可以对这个属性进行删除
del bs.a['class']
print(bs.a)
```

**4.2、NavigableString**
既然我们已经得到了标签的内容，那么问题来了，我们要想获取标签内部的文字怎么办呢？很简单，用
.string 即可，例如

```python
from bs4 import BeautifulSoup
file = open('./aa.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser")
print(bs.title.string)
print(type(bs.title.string))
```

**4.3、BeautifulSoup**
BeautifulSoup对象表示的是一个文档的内容。大部分时候，可以把它当作 Tag 对象，是一个特殊的
Tag，我们可以分别获取它的类型，名称，以及属性，例如：

```python
from bs4 import BeautifulSoup
file = open('./aa.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser")
print(type(bs.name))
print(bs.name)
print(bs.attrs)
```

**4.4、Comment**
Comment 对象是一个特殊类型的 NavigableString 对象，其输出的内容不包括注释符号。

```python
from bs4 import BeautifulSoup
file = open('./aa.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser")
print(bs.a)
# 此时不能出现空格和换行符，a标签如下：
# <a class="mnav" href="http://news.baidu.com" name="tj_trnews"><!--新闻--></a>
print(bs.a.string) # 新闻
print(type(bs.a.string)) # <class 'bs4.element.Comment'>
```



**五、遍历文档树**
5.1 .contents：获取Tag的所有子节点，返回一个list

```python
# tag的.content 属性可以将tag的子节点以列表的方式输出
print(bs.head.contents)
# 用列表索引来获取它的某一个元素
print(bs.head.contents[1])
```

5.2 .children：获取Tag的所有子节点，返回一个生成器

```python
for child in bs.body.children:
print(child)
```

5.3、.descendants：获取Tag的所有子孙节点
5.4、.strings：如果Tag包含多个字符串，即在子孙节点中有内容，可以用此获取，而后进行遍历
5.5、.stripped_strings：与strings用法一致，只不过可以去除掉那些多余的空白内容
5.6、.parent：获取Tag的父节点
5.7、.parents：递归得到父辈元素的所有节点，返回一个生成器
5.8、.previous_sibling：获取当前Tag的上一个节点，属性通常是字符串或空白，真实结果是当前标签
与上一个标签之间的顿号和换行符
5.9、.next_sibling：获取当前Tag的下一个节点，属性通常是字符串或空白，真是结果是当前标签与下
一个标签之间的顿号与换行符
5.10、.previous_siblings：获取当前Tag的上面所有的兄弟节点，返回一个生成器
5.11、.next_siblings：获取当前Tag的下面所有的兄弟节点，返回一个生成器
5.12、.previous_element：获取解析过程中上一个被解析的对象(字符串或tag)，可能与
previous_sibling相同，但通常是不一样的
5.13、.next_element：获取解析过程中下一个被解析的对象(字符串或tag)，可能与next_sibling相同，
但通常是不一样的
5.14、.previous_elements：返回一个生成器，可以向前访问文档的解析内容
5.15、.next_elements：返回一个生成器，可以向后访问文档的解析内容
5.16、.has_attr：判断Tag是否包含属性



六、搜索文档树
6.1、find_all(name, attrs, recursive, text, **kwargs)

在上面的例子中我们简单介绍了find_all的使用，接下来介绍一下find_all的更多用法-过滤器。这些过滤
器贯穿整个搜索API，过滤器可以被用在tag的name中，节点的属性等。
**（1）name参数：**
字符串过滤：会查找与字符串完全匹配的内容

```python
a_list = bs.find_all("a")
print(a_list)
```

正则表达式过滤：如果传入的是正则表达式，那么BeautifulSoup4会通过search()来匹配内容

```python
from bs4 import BeautifulSoup
import re
file = open('./aa.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser")
t_list = bs.find_all(re.compile("a"))
for item in t_list:
print(item)
```



### 3.4保存数据

- Excel表存储
  - 利用python库*xlwt*将抽取的数据*datalist*写入Excel表格
