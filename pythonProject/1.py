# -*- coding = utf-8 -*-
# @Time : 2021/11/2410:25
# @Author : 瑛
# @File : 1.py
# @Software : PyCharm

'''
print("我的名字%s,年龄%d"%("瑛",18))#我的名字瑛,年龄18

print("aaa","bbb","ccc")#aaa bbb ccc
print("www","baidu","com",sep=".")#www.baidu.com

print("hello",end="\t")
print("world",end="")
print("!",end="\n")
print("第二行")
#hello	world!
#第二行
'''

#导演: 罗伯·莱纳 Rob Reiner   主演: 玛德琳·卡罗尔 Madeline Carroll / 卡... 2010 / 美国 / 剧情 喜剧 爱情
import re
bds = "导演: 罗伯·莱纳 Rob Reiner   主演: 玛德琳·卡罗尔 Madeline Carroll / 卡... 2010 / 美国 / 剧情 喜剧 爱情"
bd = "导演: 比利·怀尔德 Billy Wilder   主演: 泰隆·鲍华 Tyrone Power / 玛琳·...<br/>1957 / 美国 / 剧情 犯罪 悬疑"
y = bd.split('/')[-2]
print(y)
