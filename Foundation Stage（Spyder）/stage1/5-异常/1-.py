# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:51:53 2021

@author: 瑛
"""
#捕获所有异常
try:
    print(f)
except Exception as result:
    print("产生错误")
    print(result)

#try finally和嵌套:finally一定执行
import time
try:
    f = open("12.txt","r")
    try:
        while True:
            content = f.readline()
                if len(content) == 0:
                    break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭了")
        
except Exception as result:
    print("产生错误")
    print(result)
    
    
    