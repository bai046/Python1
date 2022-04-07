# -*- coding = utf-8 -*-
# @Time : 2022/4/722:44
# @Author : 瑛
# @File : 网页视频保存.py
# @Software : PyCharm
# https://crcdn.ydstatic.com/xuetang/202204/02b46cef9f0f/bd_02b46cef9f0f_20220406195632.mp4
import requests

url = "https://crcdn.ydstatic.com/xuetang/202204/f4431656d6e1/bd_f4431656d6e1_20220407195711.mp4"
# 视频为二进制文件，获取content
mp4 = requests.get(url).content
# 写入文件
with open('./{0}.mp4'.format("视频test"),'wb') as f:
    f.write(mp4)
