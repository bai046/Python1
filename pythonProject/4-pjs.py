# -*- coding = utf-8 -*-
# @Time : 2021/11/3010:24
# @Author : 瑛
# @File : 4-pjs.py
# @Software : PyCharm
import requests
from bs4 import BeautifulSoup
import json
# 1，找到所爬数据所在js
url =" https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=65540518957&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"
}
response = requests.get(url, headers=headers)
html = response.text
new_html = html.lstrip("fetchJSON_comment98(").rstrip(");")
html = json.loads(new_html)  # 转换成json格式
print(html['hotCommentTagStatistics'])
# print(html['hotCommentTagStatistics'][0]['name'])
database = html['hotCommentTagStatistics']
datas = []
for num in range(0,len(database)):
    i = database[num]['name']
    j = database[num]['count']
    data = i+str(j)
    datas.append(data)
print(datas)

