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
from xlwt import *

# print(i)
url="http://industry.wanfangdata.com.cn/qd/Detail/Patent?id=Patent_CN201610938369.6"
resp=request.urlopen(url)
soup=BeautifulSoup(resp.read().decode("utf-8"),"html.parser")  #指定解析器
listUrls=soup.findAll("tr")
Title=soup.find("title")
Title=Title.get_text()
# print(Title)
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
w = Workbook(encoding="utf-8")
ws = w.add_sheet("sheet1", cell_overwrite_ok=True)




ws.write(1,0,Title)
for v,k in dic.items():
    print(v+" "+k)
    if v=='专利类型：':
        ws.write(1,1,k)
    if(v=='申请（专利）号：'):
        ws.write(1,2,k)
    if(v=='申请日期：'):
        ws.write(1,3,k)
    if(v=='公开(公告)日：'):
        ws.write(1,4,k)
    if(v=='公开(公告)号： '):
        ws.write(1,5,k)
    if(v=='主分类号：'):
        ws.write(1,6,k)
    if(v=='分类号：'):
        ws.write(1,7,k)
    if(v=='申请（专利权）人：'):
        ws.write(1,8,k)
    if(v=='发明（设计）人：'):
        ws.write(1,9,k)
    if(v=='主申请人地址：'):
        ws.write(1,10,k)
    if(v=='专利代理机构：'):
        ws.write(1,11,k)
    if(v=='代理人：'):
        ws.write(1,12,k)
    if(v=='国别省市代码：'):
        ws.write(1,13,k)





w.save("../resource/sigleTest.xls")