# -*- coding = utf-8 -*-
# @Time : 2021/11/2921:33
# @Author : 瑛
# @File : testurllib.py
# @Software : PyCharm
import urllib.request

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  # 对获取网页源码进行utf-8解码

# 获取post请求
# import urllib.parse  # 解析包
# data = bytes(urllib.parse.urlencode({"Hello": "world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)  # 用data封装post数据（模拟用户真实登入）
# print(response.read().decode("utf-8"))

# 超时处理0.01
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

# response = urllib.request.urlopen("http://httpbin.org/get")
# print(response.status)  # 200
# response = urllib.request.urlopen("http://douban.com")
# print(response.status)  # 418（我是一个茶壶）被识别为爬虫

# response = urllib.request.urlopen("http://baidu.com")
# print(response.getheaders())

# url = "http://httpbin.org/post"
# header = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"}
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,header=header,method="POST")    # 封装请求对象
# response = urllib.request.urlopen(req)  # 访问响应对象
# print(response.read().decode("utf-8"))  # 解析

url = "http://douban.com"
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"}
req = urllib.request.Request(url=url,header=header)    # 封装请求对象
response = urllib.request.urlopen(req)  # 访问响应对象
print(response.read().decode("utf-8"))  # 解析