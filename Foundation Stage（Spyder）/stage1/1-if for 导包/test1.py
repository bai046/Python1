#编程第一步

'''
#python导入包的三种方式
#第一种：import *
import random
#第二种：from * import *
from math import ceil,fabs,floor
#不建议：from math import *
#第三种：import *(包) as *(别名)
import numpy as np
import pandas as pd
#第四种：以文件导包
from my_module1 import sum_num
'''

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

'''
其中代码 a, b = b, a+b 的计算方式为先计算右边表达式，然后同时赋值给左边，等价于：
n=b
m=a+b
a=n
b=m

关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符:
print(b, end=',') 
'''
   

age=int(input("请输入年龄："))
if age > 18:
    print("该结婚了！")
else:
    print("学习！")

age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age -2)*5
    print("对应人类年龄: ", human)
 
### 退出提示
input("点击 enter 键退出")



# 该实例演示了数字猜谜游戏
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))
 
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")


n = 100
 
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,sum))

count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
   
   
flag = 1
 
while (flag): print ('欢迎访问菜鸟教程!')
 
print ("Good bye!")


sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

#遍历数字序列，可以使用内置range(start，stop，step)函数,顾头不顾尾。它会生成数列
for i in range(0, 10, 3) :
    print(i)

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])
    
    
#使用range()函数来创建一个列表：
list(range(5))
[0, 1, 2, 3, 4]

'''
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，
任何对应的循环 else 块将不执行。

continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 
false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。
'''

#如下实例用于查询质数的循环例子:
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
        
#第一步：初始化循环次数
i = 1
#第二步：编制循环条件
while i<=5:
#第三步：编制循环内容
    if i==3:
        #第五步：吃到第三个苹果有虫跳过
        print("第{0}苹果有虫，吃下一个苹果".format(i))
        i+=1
        continue
    #第四步：吃第i个苹果
    print("吃第{0}苹果".format(i))
    i+=1
    
#pass是空语句，是为了保持程序结构的完整性。一般用做占位语句，如下:
for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")



sum=0
for i in range(1,101):
    sum=sum+i
print(sum)
   

fruits='苹果3个,香蕉4个,哈密瓜8个'
sumfruits=0
x=0
for i in range(len(fruits)):
    if fruits[i]=='个':
        sumfruits=sumfruits + int(fruits[i-1])
        x+=1
print("总共有{0}类，{1}个水果".format(x,sumfruits))



for i in range(1,10):
    for j in range(1,i+1):
        print("{0}*{1}={2}".format(i,j,i*j),end="\t")
    print("\n")
    























