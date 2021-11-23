# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:24:01 2021

@author: 瑛
*步骤 ：先中文问题描述在写代码
"""
"""
from Package.time import Format_LocalTime_ToFileName    

input_filename = input("输入：")
dot_index = input_filename.rfind(".")
#print(dot_index)
if dot_index > 0:
    file_name= input_filename[:dot_index]
    #print(file_name)
    file_type= input_filename[dot_index:]
    #print(file_type)
    
    new_filename = file_name + Format_LocalTime_ToFileName() + "-[备份]" +file_type
    #print(new_filename)
    
    old_file = open(input_filename, "r",encoding="utf-8")
    new_file = open(new_filename, "w",encoding="utf-8")
    
    while True:
        content = old_file.read()
        if len(content) ==0:
            print("备份文件为空！")
            break
        new_filename.write(content) 
        
        old_file.close()
        new_file.close()
        print('备份前的文件名字：',input_filename)
        print('备份后的文件名字：',new_filename)
else:
    print("备份文件不存在！")
"""

#批量添加删除前缀 文件夹B190109
import os
path = r'D:\Python\Foundation Stage\stage1\classwork5\B190109'
os.chdir(path)
print(os.getcwd())
old_names = os.listdir( path )  #取路径下的文件名，生成列表
print(old_names)
mark = 'B190109-'
f = int(input("请输入操作（1-添加字符，2-删除字符）："))
#遍历列表下的文件名
for old_name in old_names:
    if f == 1:         
        os.rename(os.path.join(path,old_name),os.path.join(path,mark+old_name))  #重命名文件
        print(old_name,"New name is: ",mark+old_name)
    elif f == 2:
        newName = old_name.replace(mark,"")#新文件名   
        os.rename(os.path.join(path,old_name),os.path.join(path,newName))  #重命名文件
        print(old_name,"New name is: ",newName)
    else:
        print("请输入正确操作（1-添加字符，2-删除字符）")    










