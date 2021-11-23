# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:25:12 2021

@author: 瑛
numpy操作文件：D:\Python\Foundation Stage\stage1\4-Numpy包\dataset
读取，保存，curd增删改查
"""
import numpy as np

file = np.loadtxt("./dataset/db.txt",skiprows=1,usecols=(0,1))
print(file)
print("-"*30)

#file2 = np.transpose(file)
#file2 = file.T
#当遇到 行向量或者列向量的时候，转置必须使用reshape()
#file2 = file.reshape(25,1)
#print(file2)
#print(file2.shape)

file3 = np.loadtxt("./dataset/豆瓣电影数据.csv",skiprows=1,dtype=str,usecols=(0,1))
print(file3)


