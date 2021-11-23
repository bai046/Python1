# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:21:34 2021

@author: 瑛
"""



def Read_Write_File(filePath,mode_Type,Ope_Choice,size = None):
    '''
    filePath:   为文件路径+文件名 例如：D:\Python\Foundation Stage\stage1\text.text
    mode_Type:  r|w|a
    size:       读取内容的大小，默认为None，整型
    Ope_Choice: 读写操作read|write
    '''
    if Ope_Choice == "read":
        f = open("filePath","mode_Type","Ope_Choice",encoding="utf-8")
        print(f.read(size))
        f.close()
    elif Ope_Choice == "write":
        f = open("filePath","mode_Type","Ope_Choice",encoding="utf-8")
        print(f.write("write写了这个文件"))
        f.close()
    else:
        print("请填写操作类型（read|write）")

import csv
def Read_CSV_TOList(filePath,fileName):
    '''
    完整文件路径（D:\Python\Foundation Stage\stage1+text.py）
    filePath:D:\Python\Foundation Stage\stage1
    fileName:text.py
    '''
    full_FilePath = filePath + fileName
    f = open(full_FilePath,mode="r",encoding="utf-8")
    Lines = csv.reader(f)
    data = []# 用来保存csv里数据
    for line in Lines:
        data.append(line)
    return data

    """
import os,sys                       #导入模块
def add_prefix_files():             #定义函数名称
    mark = 'B190109-'                 #准备添加的前缀内容
    old_names = os.listdir( path )  #取路径下的文件名，生成列表
    for old_name in old_names:      #遍历列表下的文件名
            if  old_name!= sys.argv[0]:  #代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
               if old_name.endswith('.txt'):   #当文件名以.txt后缀结尾时
                    os.rename(os.path.join(path,old_name),os.path.join(path,mark+old_name))  #重命名文件
                    print (old_name,"has been renamed successfully! New name is: ",mark+old_name)  #输出提示

if __name__ == '__main__': 
        path = r'D:\Python\Foundation Stage\stage1\B190109'   #运行程序前，记得修改主文件夹路径！
        add_prefix_files()         #调用定义的函数，注意名称与定义的函数名一致
"""

import os
#path--文件路径
#old--要替换的字符串
#new--替换后的字符串
def bunchFileRename(path,old,new):    
    files = os.listdir(path)
    for file in files:
        oldDir=os.path.join(path,file)#原来的文件路径
        if os.path.isdir(oldDir):
            continue
        newName = file.replace(old,new)#新文件名
        newDir = os.path.join(path,newName)#新文件路径    
        os.rename(oldDir,newDir)#重命名






