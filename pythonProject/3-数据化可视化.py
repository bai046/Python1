# -*- coding = utf-8 -*-
# @Time : 2021/11/2418:13
# @Author : 瑛
# @File : 3-数据化可视化.py
# @Software : PyCharm

import matplotlib.pyplot as plt
import pandas as pd
#使用collections模块下的Counter类
from collections import Counter

def ShowDatas():
    # 1，准备数据
    df = pd.read_excel("./豆瓣电影Top250.xls", usecols=["排名", "评分", "年份"])
    df_li = df.values.tolist()
    ins = []
    rates = []
    c20 = 0
    c21 = 0
    y = []
    for s_li in df_li:
        ins.append(int(s_li[0]))
        rates.append(s_li[1])
        if s_li[2] >=2000:
            c20+=1
        else:
            c21+=1
        y.append(int(s_li[2]))
    print(ins)
    print(rates)
    print(c20)
    print(c21)
    print(y)

    # 2.1，评分与评价人数
    df = pd.DataFrame({"rates": rates,
                       "years": y,
                       "ins": ins
                       })
    ax = df.plot.bar("ins", "years",linewidth=5.0, color="yellow")
    ax.set_ylim(1955, 2011)
    df.plot("ins", "rates", secondary_y=True, ax=ax)

    # 2.2，饼状图
    # 添加图形对象
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    # 使得X/Y轴的间距相等
    ax.axis('equal')
    langs = ['20century', '21century']
    count = [c20, c21]
    # 绘制
    ax.pie(count, labels=langs, autopct='%1.2f%%')

    # 3，展示
    plt.show()

