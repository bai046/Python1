# -*- coding = utf-8 -*-
# @Time : 2022/3/1414:50
# @Author : 瑛
# @File : txts.py
# @Software : PyCharm

import re
import requests
from bs4 import BeautifulSoup
import os

# 创建作者文件用于存储
os.mkdir('./非天夜翔')

# 第一层：进入作者小说列表，拿到全部小说页面链接
for i in range(1,3):
    if i == 1:
        url = "https://www.52shuku.vip/zuozhe/feitianyexiang/index.html"
    else:
        url = "https://www.52shuku.vip/zuozhe/feitianyexiang/index_"+str(i)+".html"
    # 直接爬取
    response = requests.get(url)
    # 乱码解析
    response.encoding = 'utf-8'
    html = response.text
    # print(html)
    # 拿去所需数据数据
    soup = BeautifulSoup(html, "html.parser")
    # print(soup.find_all("article"))
    # print(soup.find_all("article")[1:])
    c = soup.find_all("article")[1:]
    # listsurl = soup.find_all("a")
    # print(listsurl)

    # 第二层：进入一本小说，拿到每页点击链接
    for item in range(0,len(c)):
        # 每一页链接
        # print(item)
        urlc = c[item].find('a').get("href")
        # print(urlc)
        # 直接爬取
        response = requests.get(urlc)
        # 乱码解析
        response.encoding = 'utf-8'
        html = response.text
        # print(html)
        # 拿去所需数据数据
        soup = BeautifulSoup(html, "html.parser")
        # print(soup.h1.string)
        name = soup.h1.string
        article_list = soup.article.ul
        # print(article_list)
        # 提取简介
        # for item in article.find_all("p"):
        #     print(item.get_text())

        # 1.存储（创建书名TXT文件）
        with open(r'./非天夜翔/{0}.txt'.format(name), 'w+',encoding='utf-8') as f:
            print(1)

        # 第三层：提取页链接——小说页面内容（大多数一致，一些不一致）
        for item in article_list.find_all("a"):
            # 每一页链接
            urls = item.get("href")
            # print(urls)
            # 直接爬取
            response = requests.get(urls)
            # 乱码解析
            response.encoding = 'utf-8'
            html = response.text
            # print(html)
            # 解析数据
            soup = BeautifulSoup(html, "html.parser")
            # print(soup)
            articles = soup.article.find_all("p")
            # print(soup.article.find("div"))
            # end = '<div class="pagination2">'
            # print(str(article[0:-3]).replace('<p>', '\r\n').replace('</p>', ''))
            a = str(articles[0:-3]).replace('<p>','\r\n').replace('</p>,','').replace('</p>','').replace('[', '').replace(']', '\r\n')
            # print(str(article[-3:-2]).split('<div')[0].replace('[<p>',''))
            b = str(articles[-3:-2]).split('<div')[0].replace('[<p>', '')

            # 2.存储（写入内容）
            with open('./非天夜翔/{0}.txt'.format(name),'a',encoding='utf-8') as f:
                f.write(a)
                f.write(b)
                print(2)