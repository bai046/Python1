# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 11:21:09 2021

@author: 瑛
"""
import pandas as pd
df4 = pd.read_csv("./dataset/green_tripdata_2014-04.csv", header=0,nrows=20)
df5 = pd.read_excel("./dataset/green_tripdata_2014-05.csv", header=0,nrows=20)

#打印列名
print(df4.columns)
'''
Index(['VendorID', 'lpep_pickup_datetime', 'Lpep_dropoff_datetime',
       'Store_and_fwd_flag', 'RateCodeID', 'Pickup_longitude',
       'Pickup_latitude', 'Dropoff_longitude', 'Dropoff_latitude',
       'Passenger_count', 'Trip_distance', 'Fare_amount', 'Extra', 'MTA_tax',
       'Tip_amount', 'Tolls_amount', 'Ehail_fee', 'Total_amount',
       'Payment_type', 'Trip_type '],
      dtype='object')
'''
#取单列
print(df4['Pickup_longitude'])
#多列location  loc[行,列]
print(df4.loc[:,['VendorID','lpep_pickup_datetime']])
print(df4.loc[0:5,1:4])



all_csv = pd.concat([df4, df5])
all_csv.to_csv('test2.csv')


