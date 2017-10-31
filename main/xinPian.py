# -*- coding: utf-8 -*-
# @Time    : 2017/10/31 上午10:49
# @Author  : SkullFang
# @Email   : yzhang_wy@163.com
# @File    : xinPian.py
# @Software: PyCharm
from urllib import request
from urllib.error import HTTPError,URLError
from bs4 import  BeautifulSoup
import datetime
import re
from xlwt import *

listTitle=[]
listStr=[]
lenth=0
# 写入操作
w = Workbook(encoding="utf-8")
ws = w.add_sheet("sheet1", cell_overwrite_ok=True)
for i in range(1,2):
    # print(i)
    url="http://industry.wanfangdata.com.cn/qd/Column/Patent?p="+str(i)+"&n=10&q=%E4%B8%93%E5%88%A9%E5%90%8D%E7%A7%B0%3A%22%E8%8A%AF%E7%89%87%22&o=sortby%20F_ApplicationDate/weight=3%20relevance/weight=1"

    resp=request.urlopen(url)
    # print(resp.getcode())
    soup=BeautifulSoup(resp.read().decode("utf-8"),"html.parser")  #指定解析器
    listUrls=soup.findAll("a",href=re.compile(r'(.+)(Detail)(.+)'));
    for url in listUrls:
        if not re.search("\.(jpg|RNG|JPG|png)", url["href"]):
            titlei=url.get_text()
            stri="http://industry.wanfangdata.com.cn"+url["href"]
            print(titlei+" "+stri)
            listTitle.append(titlei)
            listStr.append(stri)
            lenth=lenth+1



for i in range(lenth):
    ws.write(i,0,i+1)
    ws.write(i, 1, listTitle[i])
    ws.write(i, 2, listStr[i])


w.save("../resource/xinPianUrl.xls")
