# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:14:08 2021

@author: 瑛
"""
import pandas as pd
pd = pd.read_csv("./dataset/green_tripdata_2014-04.csv", header=0,nrows=10, encoding='utf-8', dtype=str)
pd2 = pd.read_csv("./dataset/green_tripdata_2014-05.csv", header=0,nrows=10, encoding='utf-8', dtype=str)
print(pd)
#True,False
pd.rename(columns={"Pickup_longitude":"上车经度"
                   ,"Pickup_latitude":"上车纬度"
                   ,"Dropoff_longitude":"下车经度"
                   ,"Dropoff_latitude":"下车纬度"
                   ,"Passenger_count":"乘客人数"
                   ,"Fare_amount":"费用"},inplace=True)
print(pd.columns)
'''
2、删除数据为0或者为空的数据（去找删除数据的api）,
取出Pickup_longitude（>-73.89）、Pickup_latitude(<40.8)、
Dropoff_longitude(>-73.9)、Dropoff_latitude(<40.8)的数据
'''
dpd = pd[pd['上车经度']!=0]
#dpd = pd.drop(index=pd[pd['Pickup_longitude']==0].index[0])
print(dpd)

dataset = dpd.loc[(dpd['上车经度'].astype(float) >-73.89) | (dpd['上车纬度'].astype(float) <40.8)| (dpd['下车经度'].astype(float) >73.9)| (dpd['下车纬度'].astype(float) <40.8)
, ['上车经度','上车纬度','下车经度','下车纬度']]
print(dataset)
dataset2 = pd2.loc[(dpd['Pickup_longitude'].astype(float) >-73.89) | (pd2['Pickup_latitude'].astype(float) <40.8)| (pd2['Dropoff_longitude'].astype(float) >73.9)| (pd2['Dropoff_latitude'].astype(float) <40.8)
, ['Pickup_longitude','Pickup_latitude','Dropoff_longitude','Dropoff_latitude']]
print(dataset2)



