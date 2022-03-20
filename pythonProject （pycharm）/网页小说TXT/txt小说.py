# -*- coding = utf-8 -*-
# @Time : 2022/3/108:40
# @Author : 瑛
# @File : txt小说.py
# @Software : PyCharm
import re
import requests
from bs4 import BeautifulSoup

for i in range(18,68):
    url = "http://m.ttcwen.com/cw/1599372462/"+str(193300+i)+".html"
    # 直接爬取
    response = requests.get(url)
    # 乱码解析
    response.encoding = 'utf-8'
    html = response.text
    # print(html)
    # 解析数据
    soup = BeautifulSoup(html, "html.parser")
    # 提取章节标题
    title = soup.h1.string
    # print(title)
    txt = str(soup.select('#txt'))
    # print(txt)
    # 提取规格文字
    txts = txt.replace('<div class="txt" id="txt">',title).replace('</div>','').replace('[','').replace(']','').replace('<br/>','\n')
    # print(txts)
    with open(r'./书名.txt','a',encoding='utf-8') as f:
        # f.write(title)
        f.write(txts)

