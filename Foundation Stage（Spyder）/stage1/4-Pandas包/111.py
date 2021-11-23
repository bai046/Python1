# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:13:46 2021

@author: 瑛
1、分别取出csv文件中的Pickup_longitude、Pickup_latitude、Dropoff_longitude、Dropoff_latitude、Passenger_count、Fare_amount列，且分别将其命名为：上车经度、上车纬度、下车经度、下车纬度、乘客人数，费用

=============================例如：=====================================
Pickup_longitude、Pickup_latitude、Dropoff_longitude、Dropoff_latitude、Passenger_count、Fare_amount
         上车经度、            上车纬度、             下车经度、               下车纬度、              乘客人数，            费用
======================================================================


2、删除数据为0或者为空的数据（去找删除数据的api）
3、取出Pickup_longitude（>-73.89）、Pickup_latitude(<40.8)、Dropoff_longitude(>-73.9)、Dropoff_latitude(<40.8)的数据
4、将两个文件最终的数据最终合并在一个文件里.
"""
import pandas as pd

#,nrows=50
df4 = pd.read_csv("./dataset/green_tripdata_2014-04.csv",usecols=['Pickup_longitude','Pickup_latitude','Dropoff_longitude','Dropoff_latitude'])
#print(df4)
#print(df4.columns)
#True,False
df4.rename(columns={"Pickup_longitude":"上车经度"
                   ,"Pickup_latitude":"上车纬度"
                   ,"Dropoff_longitude":"下车经度"
                   ,"Dropoff_latitude":"下车纬度"
                   ,"Passenger_count":"乘客人数"
                   ,"Fare_amount":"费用"},inplace=True)
#print(df4.columns)
'''
'''
#删除0
dataset4 = df4[(df4['上车经度']!=0) & (df4['上车纬度']!=0) & (df4['下车经度']!=0) & (df4['下车纬度']!=0)]
#删除空
dataset_41 = dataset4.dropna(axis=0,how="any")
#取出
dataset42 = dataset_41[(dataset_41['上车经度'] >-73.89) & (dataset_41['上车纬度'] <40.8) & (dataset_41['下车经度'] >-73.9) & (dataset_41['下车纬度'] <40.8)]

'''
dataset = df4.loc[(df4['Pickup_longitude'] >-73.89) | (df4['Pickup_latitude'] <40.8) | (df4['Dropoff_longitude'] >-73.9) | (df4['Dropoff_latitude'] <40.8)
, ['Pickup_longitude','Pickup_latitude','Dropoff_longitude','Dropoff_latitude']]
'''

#,nrows=50
df5 = pd.read_csv("./dataset/green_tripdata_2014-05.csv",usecols=['Pickup_longitude','Pickup_latitude','Dropoff_longitude','Dropoff_latitude'])
#print(df4)
#print(df4.columns)
#True,False
df5.rename(columns={"Pickup_longitude":"上车经度"
                   ,"Pickup_latitude":"上车纬度"
                   ,"Dropoff_longitude":"下车经度"
                   ,"Dropoff_latitude":"下车纬度"
                   ,"Passenger_count":"乘客人数"
                   ,"Fare_amount":"费用"},inplace=True)
#print(df5.columns)
#删除0
dataset5 = df5[(df5['上车经度']!=0) & (df5['上车纬度']!=0) & (df5['下车经度']!=0) & (df5['下车纬度']!=0)]
#删除空
dataset_51 = dataset5.dropna(axis=0,how="any")
#取出
dataset52 = dataset_51[(dataset_51['上车经度'] >-73.89) & (dataset_51['上车纬度'] <40.8) & (dataset_51['下车经度'] >-73.9) & (dataset_51['下车纬度'] <40.8)]

#将两个文件最终的数据最终合并在一个文件里.
frames = [dataset42, dataset52]
all_csv = pd.concat(frames)
all_csv.to_csv('test2.csv')








