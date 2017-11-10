# -*- coding: utf-8 -*-
# @Time    : 2017/10/30 下午6:31
# @Author  : SkullFang
# @Email   : yzhang_wy@163.com
# @File    : main.py
# @Software: PyCharm
import xlrd
import random
from xlwt import *
from urllib import request
from urllib.error import HTTPError,URLError
from bs4 import  BeautifulSoup
import socket
def fun(fname,outfname):
    bk=xlrd.open_workbook(fname)
    try:
        sh=bk.sheet_by_name("sheet1")
    except:
        print("no sheet")

    nrows=sh.nrows
    ncols=sh.ncols

    urlList=[]

    for i in range(0,nrows):
        url=sh.cell_value(i,2)
        # print(str(i)+" "+url)
        urlList.append(url)

    urlSet=set(urlList)

    index=1
    w = Workbook(encoding="utf-8")
    ws = w.add_sheet("sheet1", cell_overwrite_ok=True)
    for urlS in urlSet:
        print(index)
        if urlS is None:
            continue
        try:
            re1 = request.Request(urlS)
            # 把爬虫伪装成浏览器
            re1.add_header('user-agent',
                           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
            re = request.urlopen(re1,timeout=200)
        except (HTTPError, URLError ,ConnectionResetError,socket.timeout) as e:  # 遇到相应错误就跳过
            continue
        try:
            soup = BeautifulSoup(re.read().decode("utf-8"), "html.parser")  # 指定解析器
            listUrls = soup.findAll("tr")
            Title = soup.find("title")
            Title = Title.get_text()
            # print(Title)
            # print(listUrls)
            listTitle = []
            listBody = []
            for list in listUrls:
                sublists = list.findAll("th")
                sublists2 = list.findAll("td")
                for sublist in sublists:
                    # print(sublist.get_text())
                    listTitle.append(sublist.get_text())

                for sublist2 in sublists2:
                    # print(sublist2.get_text())
                    listBody.append(sublist2.get_text())

            dic = dict(zip(listTitle, listBody))


            ws.write(index, 0, Title)
            for v, k in dic.items():
                # print(v + " " + k)
                if v == '专利类型：':
                    ws.write(index, 1, k)
                if (v == '申请（专利）号：'):
                    ws.write(index, 2, k)
                if (v == '申请日期：'):
                    ws.write(index, 3, k)
                if (v == '公开(公告)日：'):
                    ws.write(index, 4, k)
                if (v == '公开(公告)号： ' or v == '公开(公告)号：'):
                    ws.write(index, 5, k)
                if (v == '主分类号：'):
                    ws.write(index, 6, k)
                if (v == '分类号：'):
                    ws.write(index, 7, k)
                if (v == '申请（专利权）人：'):
                    ws.write(index, 8, k)
                if (v == '发明（设计）人：'):
                    ws.write(index, 9, k)
                if (v == '主申请人地址：'):
                    ws.write(index, 10, k)
                if (v == '专利代理机构：'):
                    ws.write(index, 11, k)
                if (v == '代理人：'):
                    ws.write(index, 12, k)
                if (v == '国别省市代码：'):
                    ws.write(index, 13, k)

        except (AttributeError,HTTPError, URLError ,ConnectionResetError,socket.timeout) as e:
            continue
        except UnicodeDecodeError as e:
            continue
        index += 1

    w.save(outfname)



# fun("../resource/xiTongUrl.xls","../out/xiTong.xls")
# fun("../resource/xinXingXianShiUrl.xls","../out/xinXingXianShiUrl.xls")
# fun("../resource/zhinengUrl.xls","../out/zhineng.xls")
# fun("../resource/jiChengUrl.xls","../out/jiCheng.xls")
# fun("../resource/xinPianUrl.xls","../out/xinPian.xls")
# fun("../resource/dianZiXinXi3.xls","../out/dianZiXinXi3.xls")
# fun("../resource/dianZiXinXi4.xls","../out/dianZiXinXi4.xls")
# fun("../resource/dianZiXinXi2.xls","../out/dianZiXinXi2.xls")
# fun("../resource/dianZiXinXi5.xls","../out/dianZiXinXi5.xls")
# fun("../resource/dianZiXinXi6.xls","../out/dianZiXinXi6.xls")
# fun("../resource/dianZiXinXi7.xls","../out/dianZiXinXi7.xls")
# fun("../resource/dianZiXinXi8.xls","../out/dianZiXinXi8.xls")
# fun("../resource/dianZiXinXi9.xls","../out/dianZiXinXi9.xls")

# fun("../resource/dianZiXinXi10.xls","../out/dianZiXinXi10.xls")
fun("../resource/dianZiXinXi11.xls","../out/dianZiXinXi11.xls")
# fun("../resource/dianZiXinXi12.xls","../out/dianZiXinXi12.xls")
# fun("../resource/dianZiXinXi13.xls","../out/dianZiXinXi13.xls")



