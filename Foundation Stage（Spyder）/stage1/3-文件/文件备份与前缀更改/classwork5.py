# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 08:32:35 2021

@author: 瑛

"""
#备份文件 python.txt
import os
import time
### 文件的备份步骤：
oldname = input("请输入要备份的文件名字：")
# 01 打开python.txt文件
old_file = open(oldname, "r",encoding="utf-8")
# 02 读取123.txt文件的数据
result = old_file.read()
# 03 创建一个python-时间[备份].txt文件
rtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
filename=os.path.splitext(oldname)[0]
filetype=os.path.splitext(oldname)[1]
newname = filename + "-" + rtime + "[备份]"+filetype
new_file = open(newname, "w",encoding="utf-8")
# 04 把从python.txt读取的数据 写入到python-时间[备份].txt中
new_file.write(result)
# 05 关闭文件
old_file.close()
new_file.close()
print('备份前的文件名字：',oldname)
print('备份后的文件名字：',newname)

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

#==============================================================================
# import os
# import time
# 
# name = input('请输入要备份的文件名称:')
# # 读文件
# oldFile = open(name, 'r')
# tol = oldFile.read()
# print(tol)
# 
# listName = []
# # 获取文件前缀名
# for fileName in os.listdir():
#     if os.path.splitext(fileName)[1] == '.txt':
#         fileName = os.path.splitext(fileName)[0]
#         listName.append(fileName)
# 
# # 新的文件名
# newFile = listName[0] + time.strftime("-%Y%m%d%H%M%S", time.localtime()) + '[备份].txt'
# 
# # 文件备份 ,
# file = open(newFile, 'w')
# file.write(tol)
# oldFile.close()
# file.close()
# print("备份前的文件名:", name)
# print("备份后的文件名:", newFile)
#==============================================================================

#==============================================================================
# import time
# 
# file=open('housework/Python.txt', 'r')
# print(file.read())
# new_file=input("请输入要备份的文件名称：")
# new_file=new_file[:6]+'-'+str(time.time_ns())+'[备份]'+new_file[6:10]
# file2=open(new_file,'w')
# print('备份前的名字：',file.name)
# print('备份后的名字：',file2.name)
# 
# import os
# print(os.getcwd())
# os.chdir('B190109')
# print(os.getcwd())
# a=input("请输入编号：")
# if a==1:
#  for i in os.listdir():
#       os.rename(i,'B190109-'+i)
# if a==2:
#  for i in os.listdir():
#       os.rename(i,i[8:])
#==============================================================================


