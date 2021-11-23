# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:12:40 2021

@author: 瑛
学生信息管理-函数版封装版
"""
from Package.textdef1 import add_info_name
from Package.textdef1 import add_info_age
from Package.textdef1 import add_info_mobile
from Package.textdef1 import delete
from Package.textdef1 import update
from Package.textdef1 import select

# 定义全局变量
info_list = [{"name": '张三', "mobile": '15879054953', "age": 23}]

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
            dic = {"name": add_info_name(),"age": add_info_age(),"mobile": add_info_mobile()}
            info_list.append(dic)
            print("【INFO_3】:添加成功！")
            print(dic)
        elif command == "2":
            delete()
        elif command == "3":
            update()
        elif command == "4":
            select()
        elif command == "5":
            print("【INFO_4】：所有学生信息为：")
            print(info_list)
        elif command == "6":
            print("【INFO_5】：谢谢使用，您已成功退出系统！")
            break
        else:
            print("【ERROR_7】：输入有误，请重新输入相应数字进行操作！")
            
main()

if __name__ == '__main__':
    main()

