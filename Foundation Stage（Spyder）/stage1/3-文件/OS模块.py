# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:35:01 2021

@author: 瑛
"""
#导入os模块
import os
'''
1，文件的创建，删除，移动，展示
2，文件（创建，删除，移动，展示等）
3，路径
'''
#==============================================================================
# #使用os.rename重命名
# os.rename("text.text","python.text")
# 
# #休眠20s
# import time
# time.sleep(20)
# 
# #删除文件
# os.remove("python.text")
#==============================================================================

#创建文件夹
os.mkdir("img/XX")
#切换目录~change directory
os.chdir("img/XX")
#查看当前文件夹所在目录~get current work directory
print(os.getcwd())
#返回上级目录
os.chdir("../")
print(os.getcwd())
#查看当前目录有哪些~list directory
print(os.listdir())
#删除文件夹~remove directory
os.rmdir("img/XX")
#重命名
os.rename()

#==============================================================================
# os.rmdir("img/xx")
# #递归删除
# import shutil
# shutil.rmtree("img")
#==============================================================================





