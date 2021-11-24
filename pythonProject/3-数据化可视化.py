# -*- coding = utf-8 -*-
# @Time : 2021/11/2418:13
# @Author : 瑛
# @File : 3-数据化可视化.py
# @Software : PyCharm

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("./SaveData.xls", usecols=["评分"])
df_li = df.values.tolist()
names = []
rates = []
i = 1
for s_li in df_li:
    names.append(i)
    i+=1
    rates.append(s_li[0])
print(names)
print(rates)

plt.scatter(names, rates) #统计图
plt.show()
