# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:24:07 2021

@author: 瑛
"""
import numpy as np

#四行四列
al1 = np.arange(16).reshape((4,4))
print(al1)
print(np.diag(al1))

al2 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(al2)
print(np.diag(al2))


#合并
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
#纵向vertical合并:vstack()
print(np.vstack((a1,a2)))

#横向horizontal合并居中:hstack()
print(np.hstack((a1,a2)))

#多维合并
a3 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
a4 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
al3 = np.concatenate((a3,a4),axis=1)
print(al3)

a12 = np.arange(12).reshape(3,4)
print(a12)
print(np.split(a12,3,axis=0))

#广播Broadcasting
ab = np.array([[1],
               [2],
               [3]])
ac = np.array([4,5,6])
print(ab+ac)









