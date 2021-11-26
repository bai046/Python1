# -*- coding = utf-8 -*-
# @Time : 2021/11/258:33
# @Author : 瑛
# @File : 1-.py
# @Software : PyCharm
#以年份-评论人数作为图片命名
import requests
from bs4 import BeautifulSoup
import re
# 1，爬取网页
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"}
for i in range(0, 10):
    page = i * 25
    url = "https://movie.douban.com/top250?start=" + str(page) + "&filter="
    response = requests.get(url, headers=headers)
    html = response.text

    # 2,逐一解析数据
    soup = BeautifulSoup(html, "lxml")
    content_all = soup.find_all(class_="item")
    #print(content_all)
    for content in content_all:
        imgContent = content.find('img')
        #imgName = imgContent.attrs["alt"]
        imgUrl = imgContent.attrs["src"]
        imgUrlHd = imgUrl.replace("s_ratio_poster", "m")
        imgResponse = requests.get(imgUrlHd)
        img = imgResponse.content
        content = str(content)
        #找出所有数据
        nameContent = re.compile(r"-?\d+\.?\d*").findall(content)
        print(nameContent)
        #年份
        ye = nameContent[6]
        #评论人数
        judgeNum = nameContent[10]
        # 3,保存数据
        with open(r"./pic/{0}-{1}.jpg".format(ye,judgeNum), "wb") as f:
            f.write(img)