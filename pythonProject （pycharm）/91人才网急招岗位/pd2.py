# -*- coding = utf-8 -*-
# @Time : 2021/12/413:24
# @Author : 瑛
# @File : pd2.py
# @Software : PyCharm
import re
import pandas as pd
import requests
import xlwt
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

url = "https://www.gz91.com/"
# 直接爬取
response = requests.get(url)
# 乱码解析
response.encoding = 'utf-8'
html = response.text
# print(html)
# 解析数据
soup = BeautifulSoup(html, "html.parser")
# 爬取急招模块链接
content_urls = soup.find_all(id="lmjobs")
# print(content_urls)
# 处理数据
content_urls = str(content_urls).split("</li>")
content_urls.pop()
print(type(content_urls))

datalist = []
# 遍历爬取每个岗位信息
for i in content_urls:
    print(i)
    datas = []
    content_url = re.compile(r'<a href="(.*)" target',re.S).findall(i)
    urls = content_url[0]
    print(urls)
    # 抓取单个信息
    response = requests.get(urls)
    # 乱码解析
    response.encoding = 'utf-8'
    html = response.text
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    name = soup.h1.string
    datas.append(name)  # 公司
    # 爬取数据块
    content_all = soup.find_all(class_="zw_if1")
    # print(content_all)
    content = str(content_all).split("</dd>")
    # print(content)
    # 正则 存数据
    yuexin = re.compile(r'<em style="font-size: 18px;">(.*)</em>').findall(content[0])
    datas.append(yuexin[0])  # 提供月薪
    diqu = re.compile(r'>(.*)</i>').findall(content[1])
    datas.append(diqu[0])  # 工作地区
    leixing = re.compile(r'<i>(.*)</i>').findall(content[2])
    datas.append(leixing[0])  # 职位类型
    sex = re.compile(r'<i>(.*)</i>').findall(content[3])
    datas.append(sex[0])  # 性别要求
    pnum = re.compile(r'<i id="jtstr">(.*)</i>').findall(content[4])
    datas.append(pnum[0])  # 招聘人数
    dongtai = re.compile(r'<i>(.*)</i>').findall(content[5])
    datas.append(dongtai[0])  # 上一次查看简历时间
    niany = re.compile(r'<i>(.*)</i>').findall(content[6])
    datas.append(niany[0])  # 年龄要求
    jinyan = re.compile(r'<i>(.*)</i>').findall(content[7])
    datas.append(jinyan[0])  # 工作经验要求
    dengru = re.compile(r'<i>(.*)</i>').findall(content[8])
    datas.append(dengru[0])  # 上次登录日期（招聘人动态）
    xueli = re.compile(r'<i>(.*)</i>').findall(content[9])
    datas.append(xueli[0])  # 学历要求
    jiaz = re.compile(r'<i>(.*)</i>').findall(content[10])
    datas.append(jiaz[0])  # 驾证

    datalist.append(datas)
    # print(datas)
    # print(datalist)
    # print(len(datalist))

    # 存储数据如Excel
    excel = xlwt.Workbook(encoding="utf-8")
    # 类似Excel文件中的sheet1，创建工作表
    sheet1 = excel.add_sheet('91')
    colm = ("公司", "提供月薪","工作地区", "职位类型", "性别要求", "招聘人数", "查看简历", "年龄要求", "工作经验", "登录日期", "学历要求", "车辆驾证")
    # 写入(行,列,'内容')
    for i in range(0, 12):
        sheet1.write(0, i, colm[i])  # 列名
    for i in range(0,len(datalist)):
        data = datalist[i]
        for j in range(0, 12):
            sheet1.write(i + 1, j, data[j])  # 数据
    # 保存数据表('表名.xls')
    excel.save('91.xls')

# 读取数据
df = pd.read_excel("./91.xls", usecols=["工作经验", "学历要求"])
df_li = df.values.tolist()
jinyan1 = []
xueli1 = []
# 整理数据
for s_li in df_li:
    jinyan1.append(s_li[0])
    xueli1.append(s_li[1])
print(jinyan1)
print(xueli1)
jinyan2 = {}
for item in jinyan1:
    if item not in jinyan2:
        jinyan2[item] = 1
    else:
        jinyan2[item] += 1
print(jinyan2)
xueli2 = {}
for item in xueli1:
    if item not in xueli2:
        xueli2[item] = 1
    else:
        xueli2[item] += 1
# print(xueli2)
# print(xueli2.keys())
# print(xueli2.values())

# 1柱状图
# 创建x：经验  y:出现频率
x = list(jinyan2.keys())
y = list(jinyan2.values())
plt.bar(x, y)
# 显示x轴 y轴名称
plt.ylabel("频率")
plt.xlabel("经验")
# 增加标题
plt.title("经验统计分析")
# 2饼状图
# 添加图形对象
plt.figure(figsize=(6,6))#将画布设定为正方形，则绘制的饼图是正圆
label = list(xueli2.keys())
values = list(xueli2.values())
plt.pie(values,explode=[0.01,0.01,0.01],labels=label,autopct='%1.1f%%')#绘制饼图
plt.title('性别要求饼图')#绘制标题
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()