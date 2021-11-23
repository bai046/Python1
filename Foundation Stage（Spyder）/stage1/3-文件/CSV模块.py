# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:36:02 2021

@author: 瑛

文件：123.csv 123.xlsx READ_WEITE_FILE.py
"""
#导入csv文件，一般与os文件配合使用
import csv
#~ Comma Seperated Values 逗号分隔值

f = open("123.csv",mode="r",encoding="utf-8")

Lines = csv.reader(f)

#逗号由来：(列表存储list = [1,2,3,4])
for line in Lines:
    print(line)
#==============================================================================
# ['12', '12', '12', '12']
# ['12', '12', '12', '12']
# ['12', '12', '12', '12']
# ['12', '12', '12', '12']
# ['12', '12', '12', '12']
# ['12', '12', '12', '12']
# ['12', '12', '12', '12']    
#==============================================================================

from Package.READ_WEITE_FILE import Read_CSV_TOList
# \\ 转译一下
filePath = "D:\\Python\\Foundation Stage\\stage1\\"
fileName = "123.csv"
print(Read_CSV_TOList(filePath,fileName))



