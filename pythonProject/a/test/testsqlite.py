# -*- coding = utf-8 -*-
# @Time : 2021/11/3020:50
# @Author : 瑛
# @File : testsqlite.py
# @Software : PyCharm
import sqlite3

conn = sqlite3.connect("test.db")  # 打开或创建数据库文件
print("Opened database successfully!")

