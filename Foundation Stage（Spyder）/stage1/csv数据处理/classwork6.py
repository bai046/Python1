# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 10:58:02 2021

@author: 瑛
"""
import pandas as pd

df4 = pd.read_csv("./数据文件/green_tripdata_2014-04.csv",nrows=50,usecols=['Pickup_longitude','Pickup_latitude','Dropoff_longitude','Dropoff_latitude'])
#print(df4)
#print(df4.columns)
df4.rename(columns={"Pickup_longitude":"上车经度"
                   ,"Pickup_latitude":"上车纬度"
                   ,"Dropoff_longitude":"下车经度"
                   ,"Dropoff_latitude":"下车纬度"
                   ,"Passenger_count":"乘客人数"
                   ,"Fare_amount":"费用"},inplace=True)
#print(df4.columns)
#删除0
dataset4 = df4[(df4['上车经度']!=0) & (df4['上车纬度']!=0) & (df4['下车经度']!=0) & (df4['下车纬度']!=0)]
#删除空
dataset_41 = dataset4.dropna(axis=0,how="any")
#取出
dataset42 = dataset_41[(dataset_41['上车经度'] >-73.89) & (dataset_41['上车纬度'] <40.8) & (dataset_41['下车经度'] >-73.9) & (dataset_41['下车纬度'] <40.8)]

df5 = pd.read_csv("./数据文件/green_tripdata_2014-05.csv",nrows=50,usecols=['Pickup_longitude','Pickup_latitude','Dropoff_longitude','Dropoff_latitude'])
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








