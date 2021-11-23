# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 10:40:15 2021

@author: 瑛
"""
import numpy as np
'''
'''
aa = np.array([1,2,3],dtype=np.int64 )
print(aa)#[1 2 3]
print(aa.dtype)#int64


ab = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(ab)
print(ab.shape)#(3, 3)三行三列
print(ab.shape[0])#3
print(ab.shape[1])#3
print(ab[0,0])#1
print(ab[0,:])#[1 2 3]

      
ac = np.zeros((3,4))
print(ac)
ad = np.ones((2,3))
print(ad)







