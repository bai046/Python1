# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:17:57 2021

@author: 瑛
"""
# 读取数据
#import numpy as np
import pandas as pd

data1 = pd.read_csv("./dataset/green_tripdata_2014-04.csv")
#第一题
#1.Pickup_longitude、Pickup_latitude、Dropoff_longitude、Dropoff_latitude、Passenger_count、Fare_amount列
t1 = data1.iloc[:, 5:12]
#2.分别将其命名为：上车经度、上车纬度、下车经度、下车纬度、乘客人数，费用
t2=t1.rename(
    columns={'Pickup_longitude': '上车经度', 'Pickup_latitude': '上车纬度', "Dropoff_longitude": '下车经度',
             "Dropoff_latitude": '下车纬度', 'Passenger_count': '乘客人数', 'Trip_distance': 'trip',
             'Fare_amount': '费用'})
#将t2的数据读取都test.csv的文件
t2.to_csv('test.csv')
data2=pd.read_csv("test.csv")
#第二题
#data1[data1.isin([0])] 判断data1里面全部为0的数
#1.将0取反
data2 = data2[~data2.isin([0])]  #data1.isin([0])全部取反，得到全为非0的数
#2.将空值取反
t3 = data2[~data2.isin(['null'])]  #data1.isin([‘null’])全部取反，得到全为非空的数

#第三题
"""取出Pickup_longitude（>-73.89）、Pickup_latitude(<40.8)、Dropoff_longitude(>-73.9)、
   Dropoff_latitude(<40.8)的数据
"""
data2[(data2['上车经度'] > -73.89) & (data2['上车纬度']>40.8)&
      (data2['下车经度']>-73.9)&(data2['下车纬度']<40.8)]

#第四题
#将两个文件最终的数据最终合并在一个文件里.
data3 = pd.read_csv("./dataset/green_tripdata_2014-05.csv")

frames = [data1, data3]

all_csv = pd.concat(frames)

all_csv.to_csv('test2.csv')
