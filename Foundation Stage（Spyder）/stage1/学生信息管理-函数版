# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 08:25:25 2021

@author: 瑛
学生信息管理-函数版
"""
import time
# 定义全局变量
info_list = [{"name": '张三', "mobile": '15879054953', "age": 23,"registertime":'2021-10-14 08:33:41'}]

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

def add_info_age():  # 输入年龄（18-25）
    while True:
        age = str(input("请输入年龄："))
        if int(age) in range(18,26):
            return age
        else:
            print("【ERROR_1】：年龄输入有误，请输入年龄（18-25）！")

def add_info_time(): #生成时间
    registertime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return registertime
            
def insert():
    dic = {"name": add_info_name(),"age": add_info_age(),"mobile": add_info_mobile(),"registertime":add_info_time()}
    info_list.append(dic)
    print("【INFO_1】:添加成功！")
    print(info_list)
    
def delete():  # 删除函数
    name = add_info_name()
    for i in info_list:
        if name in i.values():
            info_list.remove(i)
            print("【INFO_2】:删除成功！")
            return
    else:
        print("【ERROR_2】：查无此人，请重新输入！")


def update():  # 修改函数
    name = add_info_name()
    for i in info_list:
        if name in i.values():
            info_list[info_list.index(i)] = {"name": name, "mobile": add_info_mobile(), "age": add_info_age(),"registertime":add_info_time()}
            print("【INFO_3】:修改成功！")
            print(info_list)
            return
    else:
        print("【ERROR_3】：查无此人，请重新输入！")
        
        
def select():  # 查找函数（按姓名）
    name = add_info_name()
    for i in info_list:
        if name in i.values():
            print(i)
            return
    else:
        print("【ERROR_4】：查无此人，请重新输入！")


def main():
    while True:
        print("学生信息管理-函数版")
        print("1.增加insert-个人信息")
        print("2.删除delete-个人信息")
        print("3.修改update-个人信息")
        print("4.查询select-个人信息")
        print("5.显示所有学生信息")
        print("6.退出系统")
        print("=====================================")
        command = str(input("请输入对应数字进行操作："))
        print("-" * 30)  # 分隔线
        if command == "1":
            insert()
        elif command == "2":
            delete()
        elif command == "3":
            update()
        elif command == "4":
            select()
        elif command == "5":
            print("【INFO_5】：所有学生信息为：")
            print(info_list)
        elif command == "6":
            print("【INFO_6】：谢谢使用，您已成功退出系统！")
            break
        else:
            print("【ERROR_7】：输入有误，请重新输入相应数字进行操作！")
            
main()

if __name__ == '__main__':
    main()
