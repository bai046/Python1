# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:19:19 2021

@author: 瑛

文件
1.创建文件
2.打开 open（）文件
3.处理（读read（）写write（））文件
4.关闭 close（）文件

console:help(open)
Help on built-in function open in module io:
open(file, mode='r\w\a', buffering=-1, encoding=utf-8, errors=None, newline=None, closefd=True, opener=None)
"""

#==============================================================================
# #读文件
# f = open("text.text",mode="r",encoding="utf-8")
# f_content = f.read()
# print(f_content)
# f.close()
#==============================================================================

#==============================================================================
# #写（覆盖）文件
# f = open("text.text",mode="w",encoding="utf-8")
# w_content = f.write("write重写了这个文件")
# print(w_content)
# f.close()
#==============================================================================

#==============================================================================
# #追加文件内容
# f = open("text.text",mode="a",encoding="utf-8")
# a_content = f.write("write追加了这个内容")
# print(a_content)
# f.close()
#==============================================================================

#from Package.READ_WEITE_FILE import Read_Write_File
#Read_Write_File(filePath,mode_Type,Ope_Choice,size = None)
#f = Read_Write_File(D:\Python\Foundation Stage\stage1\text.text,"a","write")






