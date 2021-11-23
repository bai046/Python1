# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:31:30 2021

@author: 瑛

三种列表推导式
"""
#第一种基本式：变量名 = [表达式 for 变量 in 列表]
a = [i*2 for i in range(10)]
print(a)

#第二种带if：变量名 = [表达式 for 变量 in 序列 if 条件判断]
b = [i for i in range(10) if i % 2 == 0]
print(b)

#第三种嵌套型：变量 = [表达式 for 临时变量 in 序列 for 临时变量 in 序列]
c = [(i,j) for i in range(1,3) for j in range(3)]
print(c)


#练习：text
d = [i*10 for i in range(21) if i % 2 == 0]
print(d)

d1 = [i**2 for i in range(11)]
print(d1)

names = ['skdfje','sjfi','eihfjdcdjsk']
d2 = [i for i in names if len(i) > 5]
print(d2)

names1 = [['skeedfj','sefi','eihfjdceejsk'],['apple','pyple','orange','evenge']]
d3 = [j for i in names1 for j in i if j.count('e') >= 2]
print(d3)




