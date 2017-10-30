# -*- coding: utf-8 -*-
# @Time    : 2017/10/30 下午1:23
# @Author  : SkullFang
# @Email   : yzhang_wy@163.com
# @File    : single.py
# @Software: PyCharm
from urllib import request
from urllib.error import HTTPError,URLError
from bs4 import  BeautifulSoup
import datetime
import re

# print(i)
url="http://industry.wanfangdata.com.cn/qd/Detail/Patent?id=Patent_CN201610938369.6"
resp=request.urlopen(url)
soup=BeautifulSoup(resp.read().decode("utf-8"),"html.parser")  #指定解析器
listUrls=soup.findAll("tr")
# print(listUrls)
listTitle=[]
listBody=[]
for list in listUrls:
    sublists=list.findAll("th")
    sublists2=list.findAll("td")
    for sublist in sublists:
        # print(sublist.get_text())
        listTitle.append(sublist.get_text())

    for sublist2 in sublists2:
        # print(sublist2.get_text())
        listBody.append(sublist2.get_text())

dic=dict(zip(listTitle,listBody))
for v,k in dic.items():
    print(v+" "+k)