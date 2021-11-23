# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:55:53 2021

@author: 瑛
"""
import requests
from bs4 import BeautifulSoup

#1，爬取网页
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
url = "https://www.bilibili.com/read/cv7797083/"
response = requests.get(url, headers=headers)
html = response.text
    
    #2,逐一解析数据
soup = BeautifulSoup(html, "lxml")
#print(soup)
content_all = soup.find_all(class_="img-box") 
#print(content_all) 
for content in content_all:
    imgContent = content.find('img')
    imgName = imgContent.attrs["height"]
    imgUrl = imgContent.attrs["data-src"]
    #print(imgUrl)
    imgUrlHd = imgUrl.replace("//", "http://")
    imgResponse = requests.get(imgUrlHd)
    img = imgResponse.content
    #3,保存数据
    with open(r"./pic/{0}.jpg".format(imgName), "wb") as f:
        f.write(img)     
