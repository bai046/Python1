# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:21:55 2021

@author: 瑛
"""
list0=['Tom','Rose']
list1=[1,2,3,4]
list0.append("Rose")

print(list0)

list1.insert(1,"韦老师")
print(list1)

#	1 2 3	迭代
for x in (1, 2, 3): print (x,)

#字典
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
key = dict.keys()
item = dict.items()
print(key)
print(item)

for key,value in dict.items():
    print(key,value)
    

#集合set
thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
#enumerate()返回两个值（值+值的索引）
for i,j in enumerate(thisset):
    print(i,j)
    

# 元组、字典、集合、推导式（数据结构阶段）
# 数据结构~数组，栈，队列，三元组，邻接矩阵，线性表，树，图等

# 数据结构---带结构（逻辑上的关系）的数据


# 元组---数据不可发生改变
# num_list = [10, 20, 30]
# num_list[0] = 100
# print(num_list)

# 元组的定义 使用()
# tupple1 = (10, 20, 30)
# # print(type(tupple1))  #turtle
# print(tupple1)


# tupple12 = (10, "x+", 30)
# # tupple12[0] = 20  #元组中的元素不可以修改
# print(tupple12)

# 查
# 案例1：访问元组中的某个元素
# nums = (10, 20, 30, 20, 30, 20)
# print(nums[0])

# 查找某个元素在元组中出现的位置，
# 存在则返回索引下标，不存在则直接报错
# print(nums.index(20))

# 统计某个元素在元组中出现的次数
# print("个数：",nums.count(20))

# len()方法主要就是求数据序列的长度，字符串、列表、元组
# print(len(nums))


# ==================字典===============
# 空字典
# dict = {}  
# print(type(dict))

# 有数据字典
# dict2 = {"name": "Tom", "age":20, "gender":"男"}
# print(dict2)

# 字典的增加
# num2 = [1,2,3]
# num2.append(4)

# dict = {} 

# 向字典添加元素
# dict["name"] = "Cat"
# dict["age"] = 28
# print(dict)

# list--删除操作（del clear）
# dict = {"name": "Tom", "age":20, "gender":"男"}
# del dict["name"]
# print(dict)

# clear  删库跑路（先备份）
# dict.clear()
# print(dict)


# dict = {"name": "Tom", "age":20, "gender":"男"}
# dict["gender"] = "女"
# print(dict)

# 

# cat = {'name':'Tom', 'age':5, 'address':'美国纽约'}
# 案例1：使用get获取字典中某个key的value值
# namevlue = cat.values()
# print(namevlue)

# 案例2：提取person字典中的所有key
# name = cat.keys()
# print(name)

# 案例3：提取person字典中的所有value值
# item = cat.items()
# print(item)

# 字典的遍历
# for key, value in cat.items():
#     print(key,value)



# 集合
# s1 = {10, 20, 30, 40, 50}
# print(s1,type(s1))

# # 空集合
# # s2 = {}  #空集合不推荐这种方法定义
# # print(type(s2))
# s3 = set()
# print(type(s3))



# 增删改查
students = set()

# 添加
# students.add('xj')
# students.add('yg')
# print(students)

# update()方法

# list1 = ['刘备', '关羽', '赵云']
# students.update(list1)
# print(students)

# students = set()

# students.add('刘德华')
# students.add('黎明')
# 使用update新增元素
# students.update('蔡徐坤')
# print(students)


# 集合的删操作
# # 1、定义一个集合
# products = {'萝卜', '白菜', '水蜜桃', '奥利奥', '西红柿', '凤梨'}
# # 2、使用remove方法删除白菜这个元素
# products.remove('白菜')
# print(products)
# # 3、使用discard(丢弃)方法删除未知元素
# products.discard('玉米')
# print(products)
# # 4、使用pop方法随机删除某个元素
# del_product = products.pop()
# print(del_product)


# 定义一个set集合
# s1 = {'韦帅', '英标', '高源'}
# # 判断刘帅是否在s1集合中
# if '韦帅' in s1:
#     print('韦帅在s1集合中')
# else:
#     print('韦帅没有出现在s1集合中')



# 1、+加号，代表两个序列之间的连接与整合
# str1 = 'hello'
# str2 = 'world'
# print(str1 + str2)

# # 2、定义两个列表，对其数据进行整合
# list1 = ['刘备', '关羽']
# list2 = ['诸葛亮', '赵云']
# print(list1 + list2)

# # 3、定义两个元组，对其数据进行整合
# tuple1 = (10, 20)
# tuple2 = (30, 40)
# print(tuple1 + tuple2)


# 1、字符串与乘号的关系
# print('-' * 40)
# print('传智教育Python管理系统V1.0')
# print('-' * 40)

# # 2、列表与乘号的关系
# list1 = ['*']
# print(list1 * 10)

# # 3、元组与乘号的关系
# tuple1 = (10, )
# print(tuple1 * 10)




# enumerate() 返回两个值 （ 值 与 值所对应的索引）
# list1 = [10, 20, 30, 40, 50]
# for i,j in enumerate(list1):
#     print(i,j)



# 1、定义元组类型的序列
tuple1 = (10, 20, 30)
print(list(tuple1))

# # 2、定义一个集合类型的序列
set1 = {'a', 'b', 'c', 'd'}
print(list(set1))

# # 3、定义一个字典
dict1 = {'name':'刘备', 'age':18, 'address':'蜀中'}
print(list(dict1))































