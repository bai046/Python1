# -*- coding = utf-8 -*-
# @Time : 2021/11/2819:44
# @Author : 瑛
# @File : q1.py
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

# 进行SQLLite数据库操作。用于将爬到数据写入数据库
# import sqlite3

def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1，爬取网页+2,逐一解析数据
    datalist = getData(baseurl)
    savepath = "./豆瓣电影Top250.xls"
    # 3,保存数据
    SaveData(datalist, savepath)
    # 4,可视化数据分析
    df = pd.read_excel(savepath, usecols=["评分"])
    df_li = df.values.tolist()
    names = []
    rates = []
    i = 1
    for s_li in df_li:
        names.append(i)
        i += 1
        rates.append(s_li[0])
    print(names)
    print(rates)

    plt.scatter(names, rates)  # 统计图
    plt.show()


# 全局变量：创建正则表达式对象，表示规则（字符串的模式）
findLink = re.compile(r'<a href="(.*?)">')  # 影片详情链接规则
# re.S让换行符包含在字符中:忽略换行符影响
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # 电影封面图片链接规则
findTitle = re.compile(r'<span class="title">(.*)</span>')  # 片名
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')  # 评分
findJudge = re.compile(r'<span>(\d*)人评价</span>')  # 评价人数
findInq = re.compile(r'<span class="inq">(.*)</span>')  # 一句话概述
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)  # 相关内容

# 1，爬取网页
def getData(baseurl):
    datalist = []
    # 调用获取页面信息函数1次
    for i in range(0, 1):
        url = baseurl + str(i * 25)
        # 保存获取到的源码
        html = askURL(url)

    # 2,逐一解析数据
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="item"):
        print(item)#电影全部信息
        data = []  # 保存一部电影全部信息
        item = str(item)

        link = re.findall(findLink, item)[0]  # 影片详情链接
        data.append(link)  # 添加链接

        imgSrc = re.findall(findImgSrc, item)[0]
        data.append(imgSrc)  # 添加图片

        titles = re.findall(findTitle, item)
        if (len(titles) == 2):
            ctitle = titles[0]
            data.append(ctitle)  # 添加中文名
            otitle = titles[1].replace("/", "")
            data.append(otitle)  # 添加英文文名
        else:
            data.append(titles[0])
            data.append(' ')  # 存入Excel或数据库要留（英文名字）空

        rating = re.findall(findRating, item)[0]
        data.append(rating)  # 添加平均分

        judgeNum = re.findall(findJudge, item)[0]
        data.append(judgeNum)  # 添加评价人数

        inq = re.findall(findInq, item)
        if len(inq) != 0:
            inq = inq[0].replace("。", "")  # 去掉句号
            data.append(inq)  # 添加概括
        else:
            data.append(" ")  # 存入Excel或数据库要留空

        bd = re.findall(findBd, item)[0]
        bd = re.sub(r'<br(\s+)?/>(\s+)?', " ", str(bd))  # 去掉<br/>
        bd = re.sub('/', " ", bd)  # 替换/为空
        data.append(bd.strip())  # 添加内容,去掉前后空格

        # 处理好的一部电影信息放图datalist
        datalist.append(data)
    print(datalist)  # 打印所以电影提取的信息
    return datalist


# 1，得到指定一个URL的网页内容
def askURL(url):
    # 用户代理：模拟浏览器头部信息向服务器发送信息
    # 用户代理：表示告诉豆瓣服务器，本机是什么类型的机器、浏览器（本质上是告诉浏览器，本机可以接受什么水平的文件）
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"}
    # 封装
    request = urllib.request.Request(url, headers=head)
    html = ""

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")  # 对中文进行解码
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        # 打印未捕获原因
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# 3,保存数据
def SaveData(datalist, savepath):
    # 类似创建一个Excel文件
    excel = xlwt.Workbook(encoding="utf-8")
    # 类似Excel文件中的sheet1，创建工作表
    sheet1 = excel.add_sheet('豆瓣电影Top250')
    col = ("电影详情链接", "封面链接", "中文名", "英文名", "评分", "评价人数", "概述", "详细信息")
    # 写入(行,列,'内容')
    for i in range(0, 8):
        sheet1.write(0, i, col[i])  # 列名
    for i in range(0, 25):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet1.write(i + 1, j, data[j])  # 数据

    # 保存数据表('表名.xls')
    excel.save(savepath)


# 当程序执行时，程序入口
if __name__ == '__main__':
    # 调用函数
    main()
    print("爬取完毕！")