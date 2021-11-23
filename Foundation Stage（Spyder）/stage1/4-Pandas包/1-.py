# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 10:20:15 2021

@author: 瑛
"""
import numpy as np
import pandas as pd


a1 = np.array([1,2,3,4])
print(a1)
'''
[1 2 3 4]
'''
a2 = pd.Series([1,2,3,4])
print(a2)
'''
0    1
1    2
2    3
3    4
dtype: int64
'''
a3 = pd.Series([[1,2,3,4],2,3,4],[5,6,7,8])
print(a3)
'''
5    [1, 2, 3, 4]
6               2
7               3
8               4
dtype: object
'''
a4 = pd.Series([1,2,3,4],index=["我","奥","哦","啊"])
print(a4)
'''
我    1
奥    2
哦    3
啊    4
dtype: int64
'''


#DataFrame = Excel
d1 = pd.DataFrame({
    "A":1,
    "B":2,
    "C":3,
    "D":4
    },index=[1,2,3,4])
print(d1)
'''
   A  B  C  D
1  1  2  3  4
2  1  2  3  4
3  1  2  3  4
4  1  2  3  4
'''
#时间段
dates = pd.date_range("2021-11-10",periods=4)
print(dates)

index=[1,2,3,4]
d2 = pd.DataFrame({
    "Time":pd.Timestamp("2021-11-10"),            
    "A":1,
    "B":2,
    "C":3,
    "D":4
    },index=index)
print(d2)

print("复杂类型数据")
print("-"*50)
d3 = pd.DataFrame({
    "name":2, 
    "Data":np.array(["2022"]*4),
    "PHP":["AA","BB","CC","DD"],
    "中文":["我","在","江西","省"],
    "Time":dates,
    "Series":pd.Series([1,2,3,4],index=dates)   
    })
print(d3)


#pandas与numpy相结合
d4 = pd.DataFrame(np.zeros((4,4)))
print(d4)

#读取文件
df = pd.read_excel("./dataset/豆瓣电影数据.xlsx",nrows=10)
#print(df)
#查看数据大小
print(df.shape)
#列数
print(df.columns)

print(df.describe())










