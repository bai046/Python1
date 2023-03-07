# -*- coding: utf-8 -*-
"""
52 郭淑瑛
"""
#1、求阶乘 例如：5!=5*4*3*2*1
i=1
j=5
mul=1
for i in range(1,j+1):
    mul=mul*i
print("{0}!={1}".format(j,mul))


#2图形
i=1
j=1
for i in range (1,6):
    for j in range (1,i+1):
        print("*",end=" ")
    print("\n")
    
'''
3、猜数字游戏
猜数字游戏：
1.随机生成一个1～10的数字；
2.用户共有2次机会猜；
3.若用户猜测的数字大于随机生成的数，打印"猜的数字大了"
4.若用户猜测的数字小于随机生成的数，打印"猜的数字小了"
5.若用户猜测的数字等于随机生成的数，打印"恭喜，你猜对了！"，并退出循环。
'''
#
import random
#
number = random.randint(1,10)
#
print("数字猜谜游戏!")
#
i = 1
#
for i in range(1,3):
    #
    guess = int(input("请输入你猜的数字："))
    #
    if guess == number:
        #
        print("恭喜，你猜对了！")
        #
        break
    #
    elif guess < number:
        #
        print("猜的数字小了")
    #
    elif guess > number:
        #
        print("猜的数字大了")

    
#4、计算2/1 + 3/2 + 4/3 +…+(n+1)/n，写出算法的程序.
i=1
sum=0
n=10
for i in range(1,n):
        print("{0}/{1}".format(i+1,i),end="+")
        sum=i+1/i
print("={0}".format(sum))

# 第五章 实现m(n)=1/2+2/3+...+n/n+1 的计算
def caculate(n):
    sum = 0
    for x in range(n, 0, -1):
        sum = sum + x / (x + 1)
    print("sum=", sum)
caculate(99)
# https://blog.csdn.net/qq_45193872/article/details/113663786

        
#5、将1,2,3,4,5,6,7进行反转，反转结果为7,6,5,4,3,2,1
# 第一种
list = [1,2,3,4,5,6,7]
i = 0
l = int(len(list))
print("反转前的结果：",list[0:l])
for i in range(0,int(l/2)):
    tmp = list[i]
    list[i] = list[l-i-1]
    list[l-i-1] = tmp
#     list[i] = list[-(i+1)]
#     list[-(i+1)] = tmp
print("反转后的结果：",list[0:l])
# 第二种
list = '1234567'       
print(list[::-1])
        
        
        
        
        
        
        
        
        
        