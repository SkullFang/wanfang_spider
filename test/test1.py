# -*- coding: utf-8 -*-
# @Time    : 2017/10/30 下午12:21
# @Author  : SkullFang
# @Email   : yzhang_wy@163.com
# @File    : test1.py
# @Software: PyCharm
from urllib import request
from urllib.error import HTTPError,URLError
from bs4 import  BeautifulSoup
import datetime
import re
for i in range(1,1301):
    # print(i)
    url="http://industry.wanfangdata.com.cn/qd/Column/Patent?p="+str(i)+"&n=10&q=%22%E6%99%BA%E8%83%BD%E7%BB%88%E7%AB%AF%22&o=sortby%20F_ApplicationDate/weight=3%20relevance/weight=1"

    resp=request.urlopen(url)
    # print(resp.getcode())
    soup=BeautifulSoup(resp.read().decode("utf-8"),"html.parser")  #指定解析器
    listUrls=soup.findAll("a",href=re.compile(r'(.+)(Detail)(.+)'));
    for url in listUrls:
        if not re.search("\.(jpg|RNG|JPG|png)", url["href"]):
            print("http://industry.wanfangdata.com.cn"+url["href"])




