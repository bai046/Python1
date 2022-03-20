# -*- coding = utf-8 -*-
# @Time : 2021/12/1314:33
# @Author : 瑛
# @File : 软件测试可视化.py
# @Software : PyCharm

import numpy as np
import matplotlib.pyplot as plt
countries = ['收银台', '办卡申请', '会员管理', '主持人报表','总共' ]
weixiao = np.array([18, 17, 26, 19, 80])
yiban = np.array([27, 23, 18, 18, 86])
yanzhong = np.array([4, 7, 6, 2, 19])
# 此处的 _ 下划线表示将循环取到的值放弃，只得到[0,1,2,3,4]
ind = [x for x, _ in enumerate(countries)]
#绘制堆叠图
plt.bar(ind, weixiao, width=0.5, label='微小型', color='blue', bottom=yanzhong+yiban)
plt.bar(ind, yiban, width=0.5, label='一般性', color='yellow', bottom=yanzhong)
plt.bar(ind, yanzhong, width=0.5, label='严重性', color='red')
#设置坐标轴
plt.xticks(ind, countries)
plt.ylabel("缺陷个数")
plt.xlabel("模块")
plt.legend(loc="upper right")
plt.title("缺陷模块分布")
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()