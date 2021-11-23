# -*- coding: utf-8 -*
"""
Created on Fri Sep 10 9:20:49 2021

@author: 瑛
"""
'''
标准数据类型
Python3 中有六个标准的数据类型：
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）:改变会报错！！！
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
'''
#Number（数字）Python3 支持 int、float、bool、complex（复数）。
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a),isinstance(a, int), type(b), type(c), type(d))


#String（字符串）
str = 'texttext'

print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
print (str + "TEST") # 连接字符串

#使用反斜杠 \ 转义特殊字符
#如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
print("te\nnxt\n")
print(r"te\nnxt")

#List（列表）:列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
list = [ 'abcd', 786 , 2.23, 'text', 70.2 ]
tinylist = [123, 'text']

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3:1])       # 从第二个开始输出到第三个元素,步长为一
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表



def reverseWords(input):    
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1] 
    # 重新组合字符串
    output = ' '.join(inputWords)     
    return output
if __name__ == "__main__":
    input = 'I like python'
    rw = reverseWords(input)
    print(rw)

    
#Tuple（元组）:元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
#元组中的元素类型也可以不相同：

tuple = ( 'abcd', 786 , 2.23, 'python', 70.2  )
tinytuple = (123, 'python')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

#Set（集合）
sites = {'Google', 'Taobao', 'python', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉
# 成员测试
if 'python' in sites :
    print('python 在集合中')
else :
    print('python 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)         #相同字母不输出，输出集合，重复的元素被自动去掉。
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素


'''
Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：
字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
'''
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

'''
构造函数 dict() 可以直接从键值对序列中构建字典如下：
dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
>>> dict(Runoob=1, Google=2, Taobao=3)
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
'''

































