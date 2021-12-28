# -*- coding = utf-8 -*-
# @Time : 2021/11/309:52
# @Author : 瑛
# @File : testBs4.py
# @Software : PyCharm

#BeautifulSoup4将复杂的HTML文档转换成一个复杂的树形结构，每个节点都对应的是Python对象，所有对象可以归纳为4种；Tag NavigableString BeautifulSoup Comment
from bs4 import BeautifulSoup

file= open("./baidu.html", "rb")
html = file.read().encode("utf-8")
bs = BeautifulSoup(html, "html.parser")

print(type(bs))  # BeautifulSoup
print(bs.name)  # 打印bs全部内容
print(bs.title)  # title标签
print(bs.title.string)  # NavigableString标签里的内容
print(type(bs.title.string))  # Comment为特殊不包含注释<!-- -->的NavigableString标签里的内容
print(bs.a)  # Tag 拿到第一个
print(type(bs.head))
print(bs.a.attrs)  # 拿到a标签所有属性与属性值

# 文档遍历
print(bs.head.contents)
print(bs.head.contents[1])

# 文档搜索
# find_all() a标签
print(bs.find_all("a"))
# 正则 search()
import re
print(bs.find_all(re.compile("a")))  #提取包含a的标签

# 了解：传入一个函数（方法），根据函数的要求搜索--自行定义
def name_is_exit(tag):
    return tag.has_attr("name")
t_list = bs.find_all(name_is_exit)
print(t_list)

# kwargs 参数
# t_list = bs.find_all(id=" ")
# t_list1 = bs.find_all(class=True)
# t_list = bs.find_all(text =["hao123","地图“])
# t_list = bs.find_all(text = re.compile("\d"))  #带数字文本
# limit 参数限制输出个数
# t_list1 = bs.find_all(class=True,limit=3)
# for item in t_list:
#     print(item)

# css选择器
# t_list = bs.select('title')
# t_list = bs.select('.mav')  # 类名
# t_list = bs.select('#mav')  # id
# t_list = bs.select("a[class='bin']")  # a标签里bin属性
# t_list = bs.select('head > title')  # 标签关系
# t_list = bs.select('.mav~ .bri')  # 兄弟标签
# print(t_list[0].gettext())  # 那特定文本



