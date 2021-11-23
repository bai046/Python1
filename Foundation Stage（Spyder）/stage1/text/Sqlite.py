# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 10:03:28 2021

@author: 瑛
"""

"""
import sqlite3

conn = sqlite3.connect("test.db")#打开或者创建

c = conn.cursor()#获取游标

#重点在于SQL语句编写 '''保持格式语句
sql = '''
    create table company
        (id int primary key not null,
        name text not null,
        age int not null,
        address char(50),
        salary real);
'''
c.execute(sql)#执行SQL语句

conn.commit()#提交数据库操作

conn.close()#关闭数据库连接

print("Open successful!")


#插入数据

#insert into company(id,name,age,address,salary)
#value(1,'zhangshan',32,"zhangsan",8000)


#查询数据
conn = sqlite3.connect("test.db")#打开或者创建
c = conn.cursor()#获取游标
sql = "select id,name,address,salary from company"
cursor = c.execute(sql)
for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address = ",row[2])
    print("salary = ",row[3],"\n")
conn.close()#关闭数据库连接
print("查询完毕！")
"""
