# -*- coding: utf-8 -*-
# @Time    : 2017/11/3 下午1:31
# @Author  : SkullFang
# @Email   : yzhang_wy@163.com
# @File    : dianZiXinXi.py
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
for i in range(2001,3001):
    # print(i)
    url="http://industry.wanfangdata.com.cn/qd/Column/Patent?p="+str(i)+"&n=10&q=%22%E7%94%B5%E5%AD%90%E4%BF%A1%E6%81%AF%22%20or%20%22%E7%94%B5%E5%AD%90%E4%BF%A1%E6%81%AF%E4%BA%A7%E4%B8%9A%22%20or%20%22%E9%80%9A%E4%BF%A1%E8%AE%BE%E5%A4%87%22%20or%20%22%E9%AB%98%E7%AB%AF%E8%AE%A1%E7%AE%97%E6%9C%BA%22%20or%20%22%E6%99%BA%E8%83%BD%E5%A4%96%E5%9B%B4%22%20or%20%22%E6%95%B0%E5%AD%97%E8%A7%86%E5%90%AC%22%20or%20%22%E9%AB%98%E7%AB%AF%E7%94%B5%E5%AD%90%E8%AE%BE%E5%A4%87%22%20or%20%22%E9%AB%98%E7%AB%AF%E7%94%B5%E5%AD%90%E4%BB%AA%E5%99%A8%22%20or%20%22%E9%9B%86%E6%88%90%E7%94%B5%E8%B7%AF%22%20or%20%22%E6%96%B0%E5%9E%8B%E6%98%BE%E7%A4%BA%22%20or%20%22led%22%20classsort%3A%22H*%22&o=sortby%20F_ApplicationDate/weight=3%20relevance/weight=1"

    try:
        resp = request.urlopen(url, timeout=100)
        # print(resp.getcode())
        soup = BeautifulSoup(resp.read().decode("utf-8"), "html.parser")  # 指定解析器
        listUrls = soup.findAll("a", href=re.compile(r'(.+)(Detail)(.+)'));
        for url in listUrls:
            if not re.search("\.(jpg|RNG|JPG|png)", url["href"]):
                titlei = url.get_text()
                stri = "http://industry.wanfangdata.com.cn" + url["href"]
                print(str(lenth)+" "+titlei + " " + stri)
                listTitle.append(titlei)
                listStr.append(stri)
                lenth = lenth + 1
    except:
        i = i + 1
        continue

# 写入操作
w = Workbook(encoding="utf-8")
ws = w.add_sheet("sheet1", cell_overwrite_ok=True)

for i in range(lenth):
    ws.write(i,0,i+1)
    ws.write(i, 1, listTitle[i])
    ws.write(i, 2, listStr[i])


w.save("../resource/dianZiXinXi3.xls")