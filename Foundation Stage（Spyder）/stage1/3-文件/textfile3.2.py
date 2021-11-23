# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:35:00 2021

@author: 瑛
"""
#文件读写操作后自动关闭释放资源（with as）
'''
file = open("/tmp/foo.txt")
data = file.read()
file.close()

#传统的try...finally语法
file = open("/tmp/foo.txt")
try:
    data = file.read()
finally:
    file.close()
#with...as
with open("/tmp/foo.txt") as file:
    data = file.read()
'''

dict = [
      {"user1":123456},
      {"user2":123456}
      ]
with open("d.txt","w") as f2:
    for i in dict:
        for key,value in i.items():
            f2.write("{0}:{1}\n".format(key,value))


with open("d.txt","r") as f:
    #一次性读取readlines()
    content = f.readlines()
    i = 1
    for temp in content:
        print("%d:%s"%(i,temp))
        i+= 1
'''
1:user1:123456

2:user2:123456
'''        

import csv
with open("123.csv","r") as f3:
    list = []
    content = csv.reader(f3)
    for i in content:
        i.append(list)
print(list)