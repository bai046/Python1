# -*- coding = utf-8 -*-
# @Time : 2021/11/2510:36
# @Author : 瑛
# @File : qimo.py
# @Software : PyCharm
# 网页解析，获取数据
from bs4 import BeautifulSoup
# 正则表达式，进行文字匹配
import re
# 制定URL，获取网页数据。给网页就能爬
import urllib.request, urllib.error
# 进行Excel操作。用于将爬到数据写入Excel
import xlwt
# 进行数据可视化分析
import matplotlib.pyplot as plt
# 读取Excel数据
import pandas as pd

def main():
    url = "https://blog.csdn.net/rank/list/weekly"
    # 1，爬取网页+2,逐一解析数据
    datalist = getData(url)
    savepath = "./CSDN周排行Top100.xls"
    # 3,保存数据
    #SaveData(datalist, savepath)
    # 4,可视化数据分析

# 全局变量：创建正则表达式对象，表示规则（字符串的模式）

# 1，爬取网页
def getData(url):
    datalist = []
    # 调用获取页面信息函数1次
    html = askURL(url)

    # 2,逐一解析数据
    soup = BeautifulSoup(html, "html.parser")
    print(soup.prettify())
    for item in soup.find_all('div', class_="floor-rank-total-item"):
        # print(item)#电影全部信息
        data = []  # 保存一部电影全部信息
        item = str(item)


        # 处理好的一部电影信息放图datalist
        datalist.append(data)
    print(datalist)  # 打印所以电影提取的信息
    return datalist


# 1，得到指定一个URL的网页内容
def askURL(url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29"}
    # 封装
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")  # 对中文进行解码
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        # 打印未捕获原因
        if hasattr(e, "reason"):
            print(e.reason)
    #print(html)
    return html

def SaveData(datalist, savepath):
    pass

# 当程序执行时，程序入口
if __name__ == '__main__':
    # 调用函数
    main()
    print("爬取完毕！")