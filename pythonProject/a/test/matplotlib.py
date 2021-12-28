# -*- coding = utf-8 -*-
# @Time : 2021/12/711:25
# @Author : 瑛
# @File : matplotlib.py
# @Software : PyCharm
# 查看包的命令 pip list
# 安装命令 pip install matplotlib
import numpy as np
import matplotlib.pyplot as plt


# from matplotlib.font_manager import FontProperties
# 散点图

def scatter():
    # 第一步：提供数据
    x = np.random.randn(500)
    y = np.random.randn(500)
    # 第二步：找到画图的类型（线性、柱状图、饼图、环图等....）
    plt.scatter(x, y, color="r", marker="^")  # 设置图的类型
    plt.grid(color="k", ls=":", lw="0.25")  # 设置网格
    plt.title("B190109")  # 设置图的标题
    plt.xlabel("Nan")  # 设置x轴名
    plt.ylabel("nv")  # 设置y轴名
    plt.xlim(-4, 4)  # 设置x轴刻度
    plt.ylim(-4, 3)  # 设置y轴刻度


# 散点图调用
scatter()
# 第三步：展示
plt.show()
