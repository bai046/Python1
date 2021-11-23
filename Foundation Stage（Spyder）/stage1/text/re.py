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





