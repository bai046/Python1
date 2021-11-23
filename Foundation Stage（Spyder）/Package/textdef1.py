# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:11:57 2021

@author: 瑛
classwork4函数库
"""
info_list = [{"name": '张三', "mobile": '15879054953', "age": 23}]

def add_info_name():  # 输入姓名
    name = str(input("请输入姓名："))
    return name

def add_info_mobile():  # 输入个人号码
    while True:
        mobile = str(input("请输入个人号码："))
        if len(mobile) == 11:
            return mobile           
        else:
            print("【ERROR_1】：请输入11位电话！")             

def add_info_age():  # 输入年龄（17-25）
    while True:
        age = str(input("请输入年龄："))
        if int(age) in range(17,26):
            return age
        else:
            print("【ERROR_2】：年龄输入有误，请输入年龄（17-25）！")

def delete():  # 删除函数
    name = add_info_name()
    for i in info_list:
        if name in i.values():
            info_list.remove(i)
            print("【INFO_1】:删除成功！")
            return
    else:
        print("【ERROR_3】：查无此人，请重新输入！")


def update():  # 修改函数
    name = add_info_name()
    for i in info_list:
        if name in i.values():
            info_list[info_list.index(i)] = {"name": name, "mobile": add_info_mobile(), "age": add_info_age()}
            print("【INFO_2】:修改成功！")
            return
    else:
        print("【ERROR_5】：查无此人，请重新输入！")
        
        
def select():  # 查找函数（按姓名）
    name = add_info_name()
    for i in info_list:
        if name in i.values():
            print(i)
            return
    else:
        print("【ERROR_3】：查无此人，请重新输入！")


