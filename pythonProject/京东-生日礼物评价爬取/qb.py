# -*- coding = utf-8 -*-
# @Time : 2021/12/49:54
# @Author : 瑛
# @File : qb.py
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup
import json
import csv
# 绘图
from pyecharts.charts import Bar
from pyecharts import options as opts

# 女生生日礼物
page = 1
s = 1
# 翻页
for i in range(0,2):
    url = "https://search.jd.com/search?keyword=%E5%A5%B3%E7%94%9F%E7%94%9F%E6%97%A5%E7%A4%BC%E7%89%A9&psort=4&ev=13202_11322%5E3785_11316%5E&psort=4&pvid=09ae66402cee41fa80b41b2cc16442b0&page={page}&s={s}&click=0"
    page += 1
    s += 30
    # User-Agent cookie
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43",
            }
    # 封装身份请求数据
    response = requests.get(url, headers=headers)
    # 解析数据
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    # 拿出数据
    content_all = soup.find_all(class_="gl-item")
    # print(content_all)
    for content in content_all:
        # 获取每个商品id
        content_id = content.attrs["data-sku"]
        # 生成每个商品链接
        url = f"https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={content_id}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
        # 解析js数据
        res = requests.get(url, headers=headers)
        # 使用.text属性将响应消息转换成字符串
        html = res.text
        # 整理数据
        html = html.lstrip("fetchJSON_comment98(")
        html = html.rstrip(");")
        # print(html,"123")
        # 使用json.loads()将str转换成dict型
        json_data = json.loads(html)
        judges = json_data["hotCommentTagStatistics"]

        # 数据总容器
        p_dict = []
        for judge in judges:
            name = judge["name"]
            p_dict.append(name)

        # print(p_dict)

        with open("商品信息.csv", 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(p_dict)

# 读取csv数据
path = "./商品信息.csv"
es = {}
with open(path, 'r') as f:
    reader = csv.reader(f)
    # 遍历行
    for row in reader:
        # 遍历每行评价标签
        for items in row:
            # 计算标签个数
            if items not in es:
                es[items] = 1
            else:
                es[items] += 1
# 排序
es = sorted(es.items(), key=lambda d:d[1], reverse=True)  # 由大到小
esx = []
esy = []
for i in range(0, len(es)):
    esx.append(es[i])
    esy.append(es[i][1])
# 绘图
bar = Bar()
bar.add_xaxis(esx)
bar.add_yaxis("评价频次", esy)
bar.set_global_opts(title_opts=opts.TitleOpts(title="柱状图", subtitle="生日礼物评价"))
bar.render("comments.html")





