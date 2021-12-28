# -*- coding = utf-8 -*-
# @Time : 2021/11/3020:18
# @Author : 瑛
# @File : testre.py
# @Software : PyCharm

import re
pat = re.compile("A")
patten = pat.search("CBA")
print(patten)

print(re.search("asd", "asdsaasd"))  # 前re后查找对象

print(re.findall("a","advidska"))  # 前re后查找对象

#sub
print(re.sub("a","A","acdifhasia"))  # 找到acdifhasia中的a用A替换

# 建议在正则中被比较字符串前加r不用担心转义字符
print(r"\nasv\'")