# -*- coding = utf-8 -*-
# @Time : 2021/11/2410:25
# @Author : 瑛
# @File : 1.py
# @Software : PyCharm
# import numpy as np
# import pandas as pd
# from matplotlib import pyplot as plt
#
# df = pd.read_excel("./91.xls", usecols=["工作经验", "学历要求"])
# df_li = df.values.tolist()
# jinyan1 = []
# xueli1 = []
# for s_li in df_li:
#     jinyan1.append(s_li[0])
#     xueli1.append(s_li[1])
# print(jinyan1)
# print(xueli1)
# jinyan2 = {}
# for item in jinyan1:
#     if item not in jinyan2:
#         jinyan2[item] = 1
#     else:
#         jinyan2[item] += 1
# print(jinyan2)
#
# xueli2 = {}
# for item in xueli1:
#     if item not in xueli2:
#         xueli2[item] = 1
#     else:
#         xueli2[item] += 1
# print(xueli2)
# print(xueli2.keys())
# print(xueli2.values())
#
# # 1柱状图
# # 创建x：经验  y:出现频率
# x = list(jinyan2.keys())
# y = list(jinyan2.values())
# plt.bar(x, y)
# # 显示x轴 y轴名称
# plt.ylabel("频率")
# plt.xlabel("经验")
# # 增加标题
# plt.title("经验统计分析")
# # 2饼状图
# # 添加图形对象
# plt.figure(figsize=(6,6))#将画布设定为正方形，则绘制的饼图是正圆
# label = list(xueli2.keys())
# values = list(xueli2.values())
# plt.pie(values,explode=[0.01,0.01,0.01],labels=label,autopct='%1.1f%%')#绘制饼图
# plt.title('性别要求饼图')#绘制标题
# # 解决中文乱码问题
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.show()


# import csv
# from pyecharts.charts import Bar
# from pyecharts import options as opts
#
# path = "./商品信息.csv"
#
# es = {}
# with open(path, 'r') as f:
#     reader = csv.reader(f)
#     # 遍历行
#     for row in reader:
#         # 遍历每行评价标签
#         for items in row:
#             # 计算标签个数
#             if items not in es:
#                 es[items] = 1
#             else:
#                 es[items] += 1
# print(type(es))
# print(es)
# # 排序
# # d_order1=sorted(es.items(),key=lambda x:x[1],reverse=False)  # 有小到大
# # print(d_order1)
# es=sorted(es.items(), key=lambda d:d[1], reverse=True)  # 由大到小
# print(type(es))
# print(es)
# print(len(es))
# print(es[0][1])
# print(es[1][0])
# print(es[2][0])
# print(es[3][1])
# esx = []
# esy = []
# for i in range(0,len(es)):
#     esx.append(es[i])
#     esy.append(es[i][1])
#
# bar = Bar()
# bar.add_xaxis(esx)
# bar.add_yaxis("评价频次", esy)
# bar.set_global_opts(title_opts=opts.TitleOpts(title="柱状图", subtitle="生日评价"))
# bar.render("comments3.html")



'''
print("我的名字%s,年龄%d"%("瑛",18))#我的名字瑛,年龄18

print("aaa","bbb","ccc")#aaa bbb ccc
print("www","baidu","com",sep=".")#www.baidu.com

print("hello",end="\t")
print("world",end="")
print("!",end="\n")
print("第二行")
#hello	world!
#第二行
'''

#导演: 罗伯·莱纳 Rob Reiner   主演: 玛德琳·卡罗尔 Madeline Carroll / 卡... 2010 / 美国 / 剧情 喜剧 爱情
# import re
# bds = "导演: 罗伯·莱纳 Rob Reiner   主演: 玛德琳·卡罗尔 Madeline Carroll / 卡... 2010 / 美国 / 剧情 喜剧 爱情"
# bd = "导演: 比利·怀尔德 Billy Wilder   主演: 泰隆·鲍华 Tyrone Power / 玛琳·...<br/>1957 / 美国 / 剧情 犯罪 悬疑"
# y = bd.split('/')[-2]
# print(y)



# database = [{'id': '4465d4e86cd18425', 'name': '新鲜十足', 'count': 506, 'type': 4, 'canBeFiltered': True, 'stand': 1, 'rid': '4465d4e86cd18425', 'ckeKeyWordBury': 'eid=100^^tagid=4465d4e86cd18425^^pid=20002^^sku=65540518957^^sversion=1000^^token=c3b2b2cd3efdd5eb'},
#  {'id': '4a0715f0ec9e17f8', 'name': '肉质紧实', 'count': 209, 'type': 4, 'canBeFiltered': True, 'stand': 1, 'rid': '4a0715f0ec9e17f8', 'ckeKeyWordBury': 'eid=100^^tagid=4a0715f0ec9e17f8^^pid=20002^^sku=65540518957^^sversion=1000^^token=e460e9457ba0c065'},
#  {'id': 'e25d95c9cc76ae89', 'name': '品质保障', 'count': 158, 'type': 4, 'canBeFiltered': True, 'stand': 1, 'rid': 'e25d95c9cc76ae89', 'ckeKeyWordBury': 'eid=100^^tagid=e25d95c9cc76ae89^^pid=20002^^sku=65540518957^^sversion=1000^^token=ba05092c4bbfcdc0'},
#  {'id': '052519c92b2a4adf', 'name': '大小均匀', 'count': 128, 'type': 4, 'canBeFiltered': True, 'stand': 1, 'rid': '052519c92b2a4adf', 'ckeKeyWordBury': 'eid=100^^tagid=052519c92b2a4adf^^pid=20002^^sku=65540518957^^sversion=1000^^token=6c055b51d88d5860'},
#  {'id': 'afcaf4f74ca1f86a', 'name': '香甜可口', 'count': 92, 'type': 4, 'canBeFiltered': True, 'stand': 1, 'rid': 'afcaf4f74ca1f86a', 'ckeKeyWordBury': 'eid=100^^tagid=afcaf4f74ca1f86a^^pid=20002^^sku=65540518957^^sversion=1000^^token=884dc59971aadf0b'},
#  {'id': 'aa15a63e0112ff7e', 'name': '彰显档次', 'count': 19, 'type': 4, 'canBeFiltered': True, 'stand': 1, 'rid': 'aa15a63e0112ff7e', 'ckeKeyWordBury': 'eid=100^^tagid=aa15a63e0112ff7e^^pid=20002^^sku=65540518957^^sversion=1000^^token=29b726f231456cea'},
#  {'id': '07b157e8fe60d694', 'name': '肉质扎实', 'count': 18, 'type': 4, 'canBeFiltered': True, 'stand': 1, 'rid': '07b157e8fe60d694', 'ckeKeyWordBury': 'eid=100^^tagid=07b157e8fe60d694^^pid=20002^^sku=65540518957^^sversion=1000^^token=1b82a47c5ded06b2'},
#  {'id': '4fa2d72ac670a981', 'name': '食用方便', 'count': 10, 'type': 4, 'canBeFiltered': True, 'stand': 1, 'rid': '4fa2d72ac670a981', 'ckeKeyWordBury': 'eid=100^^tagid=4fa2d72ac670a981^^pid=20002^^sku=65540518957^^sversion=1000^^token=8f727feb541d71de'},
#  {'id': '0bc95c89b56d590a', 'name': '虾味十足', 'count': 3, 'type': 4, 'canBeFiltered': True, 'stand': 1, 'rid': '0bc95c89b56d590a', 'ckeKeyWordBury': 'eid=100^^tagid=0bc95c89b56d590a^^pid=20002^^sku=65540518957^^sversion=1000^^token=b45d0738c5719a70'},
#  {'id': '9481801d22638c3b', 'name': '方便易用', 'count': 3, 'type': 4, 'canBeFiltered': True, 'stand': 1, 'rid': '9481801d22638c3b', 'ckeKeyWordBury': 'eid=100^^tagid=9481801d22638c3b^^pid=20002^^sku=65540518957^^sversion=1000^^token=a0e6a671e9807137'},
#  {'id': '8664f0d55c683531', 'name': '颜色漂亮', 'count': 3, 'type': 4, 'canBeFiltered': True, 'stand': 1, 'rid': '8664f0d55c683531', 'ckeKeyWordBury': 'eid=100^^tagid=8664f0d55c683531^^pid=20002^^sku=65540518957^^sversion=1000^^token=0b360e47811c7544'},
#  {'id': 'b433a520d01fa114', 'name': '含量丰富', 'count': 1, 'type': 4, 'canBeFiltered': True, 'stand': 1, 'rid': 'b433a520d01fa114', 'ckeKeyWordBury': 'eid=100^^tagid=b433a520d01fa114^^pid=20002^^sku=65540518957^^sversion=1000^^token=63026b6ca327d686'},
#  {'id': '1892c24223f61640', 'name': '量足质优', 'count': 1, 'type': 4, 'canBeFiltered': True, 'stand': 1, 'rid': '1892c24223f61640', 'ckeKeyWordBury': 'eid=100^^tagid=1892c24223f61640^^pid=20002^^sku=65540518957^^sversion=1000^^token=3a4a54adbe3974d6'}]
# datas = []
# for num in range(0,len(database)):
#     i = database[num]['name']
#     j = database[num]['count']
#     data = i+str(j)
#     datas.append(data)
# print(datas)

# import csv
#
# header = ['name', 'age']  # 数据列名
# datas = [{'name': 'Tony', 'age': 17},
#          {'name': '李华', 'age': 21}]  # 字典数据
#
# # test.csv表示如果在当前目录下没有此文件的话，则创建一个csv文件
# # a表示以“追加”的形式写入，如果是“w”的话，表示在写入之前会清空原文件中的数据
# # newline是数据之间不加空行
# # encoding='utf-8'表示编码格式为utf-8，如果不希望在excel中打开csv文件出现中文乱码的话，将其去掉不写也行。
# with open('test.csv', 'a', newline='', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, fieldnames=header)  # 提前预览列名，当下面代码写入数据时，会将其一一对应。
#     writer.writeheader()  # 写入列名
#     writer.writerows(datas)  # 写入数据



# a = (['美味可口', '清爽不腻', '新鲜味美', '味道香浓', '方便实用', '分量充足', '奶香四溢', '含量丰富', '香气扑鼻', '食用方便', '做工精良', '美感十足'])
# print(type(a))
# print(a[0])


# a = "深圳市-计算机软件-1000-9999"
# b = a.split('-')[2]
# print(b)

# import re
# a = ['\n                            导演: 罗伯·莱纳 Rob Reiner\xa0\xa0\xa0主演: 玛德琳·卡罗尔 Madeline Carroll / 卡...<br/>\n                            2010\xa0/\xa0美国\xa0/\xa0剧情 喜剧 爱情\n                        ']
# a = re.sub(r"xa0", "", str(a))
# print(a)
# b = re.compile(r"-?\d+\.?\d*", re.S).findall(a)
# print(b)

import requests
from bs4 import BeautifulSoup

url = "https://www.52shuku.vip/chongsheng/16190_2.html"
# 直接爬取
response = requests.get(url)
# 乱码解析
response.encoding = 'utf-8'
html = response.text
# print(html)
# 解析数据
soup = BeautifulSoup(html, "html.parser")
# print(soup)
article = soup.article.find_all("p")
# print(soup.article.find("div"))
# end = '<div class="pagination2">'
print(str(article[0:-3]).replace('<p>','\r\n').replace('</p>,','').replace('</p>','').replace('[', '').replace(']', '\r\n'))
# print(str(article[-3:-2]).split('<div')[0].replace('[<p>',''))
a = str(article[-3:-2]).split('<div')[0].replace('[<p>','')
print(a)


