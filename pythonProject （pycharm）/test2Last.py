# -*- coding = utf-8 -*-
# @Time : 2021/12/308:41
# @Author : 瑛
# @File : test2Last.py
# @Software : PyCharm
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j, "*", i, "=", (i*j), end=" ", sep="")
#     print("")
#
# i = 0
# j = 0
# while i < 9:
#     i += 1
#     while j < 9:
#         j += 1
#         print(j, "*", i, "=", i*j, end="")
#         if i == j:
#             j = 0
#             print("")
#             break


#100以内质数的while循环
# i = 2
# while i < 100:
#     j = 2
#     while j < i:
#         if i % j == 0:
#             break
#         else:
#             if j == i-1:
#                 print(i)
#         j += 1
#     i += 1

# for i in range(1, 5):
#     for j in range(1, 5-i):
#         print(end=" ")
#     for k in range(5-i, 5):
#         print("*", end=" ")
#     print("")

# name = input(" = ")
# password = input(" = ")
# name_1 = "1"
# password_1 = "123"
# if name != name_1:
#     print("name!")
#     if password != password_1:
#         print("password!")
# elif password != password_1:
#     print("password!")
# else:
#     print("Hello Python")

# a = "abcdefg"
# print(a[::-1])

# student_dict = {'wang':['aa','bb'],'zhang':['bb','cc']}
# print(student_dict)
# for key,value in student_dict.items():
#     print(key,str(value))

# arr_old = ['a','b','c','s','a','b','c']
# arr_new = list(set(arr_old))
# # arr_one = list(arr_new)
# print(arr_new)
# # print(arr_one)

# arr = []
# nums = {}
# arr_my = "abcdeaABCAABCcbsab"
# new_arr = arr_my.lower()
# for o in new_arr:
#     arr.append(o)
# for i in arr:
#     if arr.count(i) >= 0:
#         nums[i] = arr.count(i)
# print(nums)

# sma = []
# students_dict = {'2':'ab','1':'b','0':'c'}
# # for key in students_dict.keys():
# #     sma.append(key)
# # a = sorted(sma)
# # for k in a:
# #     print(students_dict[k])
# by_key = sorted(students_dict.items(),key=lambda item:item[0])
# print(by_key)

# 最大公约数，和最小公倍数
def demo(m,n):
    p = m*n
    while m%n!=0:
        n=m%n
    return (n,p/n)
a = int(input("1:"))
b = int(input("2:"))
c = demo(a,b)
print(c)


