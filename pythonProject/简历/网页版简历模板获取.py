# -*- coding = utf-8 -*-
# @Time : 2022/3/1914:26
# @Author : 瑛
# @File : 网页版简历模板获取.py
# @Software : PyCharm
import requests
from bs4 import BeautifulSoup

# 静态网页[商务简历模板列表_乔布简历 (qiaobutang.com)](https://cv.qiaobutang.com/tpl/all)：中英文简历模板
url = "https://cv.qiaobutang.com/lp/544db5810cf2f3edc4dcb6db"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,"lxml")
content_all = soup.find(class_="MuiBox-root jss13")
print(content_all)
with open(r'./moban.txt','a',encoding='utf-8') as f:
    f.writelines(str(content_all))
