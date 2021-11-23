# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 20:10:21 2021

@author: 瑛
"""
import xlwt

'''
#类似创建一个Excel文件
workExcel = xlwt.Workbook(encoding="utf-8")
#类似Excel文件中的sheet1，创建工作表
worksheet1 = workExcel.add_sheet('sheet1')
#写入(行,列,'内容')
worksheet1.write(0,0,'hello')
#保存数据表('表名.xls')
workExcel.save('firsttext.xls')
'''


workExcel = xlwt.Workbook(encoding="utf-8")
#类似Excel文件中的sheet1，创建工作表
worksheet1 = workExcel.add_sheet('sheet1')
#写入(行,列,'内容')
for i in range(0,9):
    for j in range(0,i+1):
        worksheet1.write(i,j,"%d*%d=%d"%(i+1,j+1,(i+1)*(j+1)))
#保存数据表('表名.xls')
workExcel.save('九九乘法表.xls')



