# -*- coding = utf-8 -*-
# @Time : 2021/11/2410:38
# @Author : 瑛
# @File : 1-图片.py
# @Software : PyCharm
import requests
from bs4 import BeautifulSoup

# 1，爬取网页
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"}
for i in range(0, 2):
    page = i * 25
    url = "https://movie.douban.com/top250?start=" + str(page) + "&filter="
    response = requests.get(url, headers=headers)
    html = response.text

    # 2,逐一解析数据
    soup = BeautifulSoup(html, "lxml")
    content_all = soup.find_all(class_="pic")
    for content in content_all:

        imgContent = content.find(name="img")

        imgName = imgContent.attrs["alt"]
        imgUrl = imgContent.attrs["src"]
        imgUrlHd = imgUrl.replace("s_ratio_poster", "m")
        imgResponse = requests.get(imgUrlHd)
        img = imgResponse.content
        # 3,保存数据
        with open(r"./pic/{0}.jpg".format(imgName), "wb") as f:
            f.write(img)
'''
#解析：https://note.youdao.com/ynoteshare/index.html?id=f78b2199f26a1bb19f0b3aff0954163c&type=note&_time=1637198903933
# 使用import导入requests模块，在爬取新的网页内容前，我们需要导入requests模块，请求并查看状态码。
import requests

# 使用from..import从bs4模块导入BeautifulSoup
# 拿到网页源代码后，使用解析库BeautifulSoup对网页进行解析，提取网页节点内容。
# beautifulsoup是一个可以从HTML或XML文件中提取数据的Python库。它能够通过你喜欢的转换器实现惯用的文档导航，查找，修改文档的方# 式。（官方），是一个解析器，可以特定的解析出内容，省去了我们编写正则表达式的麻烦。
from bs4 import BeautifulSoup

# 将User-Agent以字典键对形式赋值给headers，https://blog.csdn.net/yeyuanxiaoxin/article/details/104345734
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"}

# 使用for循环遍历range()函数生成的0-1的数字，拿去分页信息
for i in range(0, 2):

    # 取遍历中的每个数和25相乘计算每页的数值，并赋值给page
    page = i * 25

    # 用"https://movie.douban.com/top250?start="和page转换成的字符串格式相连，接着连上"&filter="，并赋值给url.	
    # for循环生成的参数属于整型，不能直接与字符串进行拼接，需要将整型转为字符串再处理。str(page)
    url = "https://movie.douban.com/top250?start=" + str(page) + "&filter="

    # 将字典headers传递给headers参数，添加进requests.get()中，赋值给response
    response = requests.get(url, headers=headers)

    # 将服务器响应内容转换为字符串形式，赋值给html
    html = response.text

    # 使用BeautifulSoup()传入变量html和解析器lxml，赋值给soup
    soup = BeautifulSoup(html, "lxml")

    # 使用find_all()查询soup中class="pic"的节点，赋值给content_all。字符串过滤
    content_all = soup.find_all(class_="pic")

#find_all(tag, attributes, recursive, text, limit, keywords)
#（标签、属性、递归、文本、限制、关键词）
#find(tag, attributes, recursive, text, keywords)


    # for循环遍历content_all。333，分别保存
    for content in content_all:

        # 使用find()查询content中的img标签，并赋值给imgContent
        imgContent = content.find(name="img")

        # 使用.attrs获取alt对应的属性值，并赋值给imgName
        imgName = imgContent.attrs["alt"]

        # 使用.attrs获取src对应的属性值，并赋值给imgUrl
        imgUrl = imgContent.attrs["src"]

        # 使用replace()函数将链接中的s_ratio_poster替换成m，并赋值给imgUrlHd
        imgUrlHd = imgUrl.replace("s_ratio_poster", "m")

#首页图片链接和高清图片的链接，两个链接非常相似，只要将图中标黄的部分替换成m，就变成了高清图片链接。
#图片的后缀名为.webp，这是Google开发的一种图片格式，网站可以使用 WebP 创建尺寸更小、细节更丰富的图片。

        # 将链接添加进requests.get()中，赋值给imgResponse
        imgResponse = requests.get(imgUrlHd)

        # 使用.content属性将响应消息转换成图片数据，赋值给imgHtml
        img = imgResponse.content

        # 使用with语句配合open()函数以图片写入的方式打开文件
        # 用格式化将图片名字和.jpg格式组合
        # 打开的文件赋值为f
        with open(r"./pic/{0}.jpg".format(imgName), "wb") as f:
            # 使用write()将图片写入
            f.write(img)         
'''



