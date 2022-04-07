# -*- coding = utf-8 -*-
# @Time : 2022/4/722:44
# @Author : 瑛
# @File : 网页视频保存.py
# @Software : PyCharm
# https:？？.mp4
import requests

# 获取视频网页URL
url = "https://？？.mp4"
# 视频为二进制文件，获取content
mp4 = requests.get(url).content
# 写入文件
with open('./{0}.mp4'.format("视频test"),'wb') as f:
    f.write(mp4)
