# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:27:01 2021

@author: 瑛
"""
#==============================================================================
# def 函数名（参数列表）:
#     函数体
#==============================================================================
#第一种：无参函数
#第二种：有参函数
#第三种：带返回值函数
#text
#随机生成四位验证码（数字）
import random
number = random.randint(1000,9999)
print(number)

#随机生成四位验证码（混合）
e = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = random.sample(e,4)
b = str(a[0]) + str(a[1]) + str(a[2]) + str(a[3])
print(b)


#局部变量 全局变量(慎用) global变量(局部当全局用)
info = []
def add_information():
    global info
    for i in range(1,3):
        info.append(1)
    print(info)
 
add_information()

def add2_information():
    for i in range(11,13):
        info.append(1)
    print(info)
 
add2_information()


#匿名函数(lambda表达式):只包含一个返回值与一句代码
#变量 = lambda 函数参数列表:表达式(函数代码 + return返回值)
#1：一般形式
aa = lambda x:x**2
print(aa(3))
#2：带if形式
max = lambda num1,num2 :num1 if (num1 > num2) else num2
print(max(4,6))
#3：直接带参
print((lambda num1,num2 :num1 if (num1 > num2) else num2)(1,3))




#列表数据按字典key的值排序
students = [
	{'name': 'TOM', 'age': 20},
	{'name': 'ROSE', 'age': 19},
	{'name': 'Jack', 'age': 22}
			]
# 按name值升序排列
students.sort(key=lambda x: x['name'])
print(students)

# 按name值降序排列
students.sort(key=lambda x: x['name'], reverse=True)
print(students)

# 按age值升序排列
students.sort(key=lambda x: x['age'])
print(students)






    
    
