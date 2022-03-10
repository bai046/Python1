# -*- coding = utf-8 -*-
# @Time : 2022/3/108:40
# @Author : 瑛
# @File : txt小说.py
# @Software : PyCharm
import re
import requests
from bs4 import BeautifulSoup

url = "http://m.ttcwen.com/cw/1599372462/193318.html"
# 直接爬取
response = requests.get(url)
# 乱码解析
response.encoding = 'utf-8'
html = response.text
print(html)
# 解析数据
soup = BeautifulSoup(html, "html.parser")
title = soup.h1.string
print(title)
txt = str(soup.select('#txt'))
print(txt)
txtcontent = ''.join(re.findall('[^\x00-\xff]',txt))
print(txtcontent)


