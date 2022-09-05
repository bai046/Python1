# -*- coding = utf-8 -*-
# @Time : 2022/5/2314:31
# @Author : 瑛
# @File : 1.py.py
# @Software : PyCharm
import time
import requests
from bs4 import BeautifulSoup


for i in range(1594098,1594175):
    time.sleep(2)  # 休眠1秒
    url = "https://www.idanmei.cc/novel/61901/" + str(i) + ".html"
    # 直接爬取
    response = requests.get(url)
    # print(response)
    # 乱码解析
    response.encoding = 'utf-8'
    html = response.text
    # print(html)
    # 解析数据
    soup = BeautifulSoup(html, "html.parser")
    title = soup.select('#booktxt')
    print(title)
    txt = str(title[0:]).replace('<p>','\r\n').replace('</p>','').replace('<div id="booktxt">', '').replace('</div>', '\r\n').replace('[', '').replace(']', '\r\n')
    print(txt)
    with open(r'./不洁.txt', 'a', encoding='utf-8') as f:
        f.write(txt)
        print(1)

