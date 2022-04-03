# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 18:59:16 2021

@author: 瑛
正则表达式：字符串模式（判断字符串是否符合一定的标准
"""
import re

#创建模式对象

#标准
pat = re.compile("AA")
#search方法 被效验的内容
m = pat.search("CBA")
#None
n = pat.search("CBAA")
#<_sre.SRE_Match object; span=(2, 4), match='AA'>
print(m)
print(n)

#re.search("规则","效验内容")
print(re.search("a","abc"))
#<_sre.SRE_Match object; span=(0, 1), match='a'>
print(re.findall("[a-z]","abc"))
#['a', 'b', 'c']
print(re.findall("[a-z]+","abcBskf"))
#['abc', 'skf']


#sub("","","")
print(re.sub("a","A","abcdaed"))
#AbcdAed

import phone
from time import *
import re
def begin():
    print("欢迎来到查询小程序")
    print("1.查询")
    print("2.用户")


def p(n):
    if re.match(r'1[3,4,5,7,8]\d{9}', n):
        if re.match(r'13[0,1,2]\d{8}', n) or \
                re.match(r"15[5,6]\d{8}", n) or \
                re.match(r"18[5,6]", n) or \
                re.match(r"145\d{8}", n) or \
                re.match(r"176\d{8}", n):
            return True
        elif re.match(r"13[4,5,6,7,8,9]\d{8}", n) or \
                re.match(r"147\d{8}|178\d{8}", n) or \
                re.match(r"15[0,1,2,7,8,9]\d{8}", n) or \
                re.match(r"18[2,3,4,7,8]\d{8}", n):
            return True
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    s = 0
    begin()
    while True:
        op = int(input("请输入:"))
        if op == 1:
            phoneNum = str(input("请输入你的电话号码"))
            if p(phoneNum) == False:
                print("该手机号无效")
                for i in range(100):
                    print('\n')
                begin()
            else:
                info = phone.Phone().find(phoneNum)
                print("手机号码:" + str(info["phone"]))
                print("手机所属地:" + str(info["province"]) + "省" + str(info["city"]) + "市")
                print("邮政编号:" + str(info["zip_code"]))
                print("区域号码:" + str(info["area_code"]))
                print("手机类型:" + str(info["phone_type"]))
                s += 1
                i = input("输入任意数退出...")
                for i in range(100):
                    print('\n')
                begin()
        if op == 2:
            print("使用次数:" + str(s))
            i = input("输入任意数退出...")
            for i in range(100):
                print('\n')
            begin()






