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

# print(i)
# url = "http://industry.wanfangdata.com.cn/qd/Column/Patent?p=2&n=10&q=%22%E7%94%B5%E5%AD%90%E4%BF%A1%E6%81%AF%22%20or%20%22%E7%94%B5%E5%AD%90%E4%BF%A1%E6%81%AF%E4%BA%A7%E4%B8%9A%22%20or%20%22%E9%80%9A%E4%BF%A1%E8%AE%BE%E5%A4%87%22%20or%20%22%E9%AB%98%E7%AB%AF%E8%AE%A1%E7%AE%97%E6%9C%BA%22%20or%20%22%E6%99%BA%E8%83%BD%E5%A4%96%E5%9B%B4%22%20or%20%22%E6%95%B0%E5%AD%97%E8%A7%86%E5%90%AC%22%20or%20%22%E9%AB%98%E7%AB%AF%E7%94%B5%E5%AD%90%E8%AE%BE%E5%A4%87%22%20or%20%22%E9%AB%98%E7%AB%AF%E7%94%B5%E5%AD%90%E4%BB%AA%E5%99%A8%22%20or%20%22%E9%9B%86%E6%88%90%E7%94%B5%E8%B7%AF%22%20or%20%22%E6%96%B0%E5%9E%8B%E6%98%BE%E7%A4%BA%22%20or%20%22led%22%20classsort%3A%22H*%22&o=sortby%20F_ApplicationDate/weight=3%20relevance/weight=1"
#
# resp = request.urlopen(url)
# # print(resp.getcode())
# soup = BeautifulSoup(resp.read().decode("utf-8"), "html.parser")  # 指定解析器
# print(soup)
# listUrls = soup.findAll("a", href=re.compile(r'(.+)(Detail)(.+)'));
# for url in listUrls:
#     if not re.search("\.(jpg|RNG|JPG|png)", url["href"]):
#         print("http://industry.wanfangdata.com.cn" + url["href"])




# class Fib(object):
#
#     def __init__(self, num):
#         L = [0, 1]
#         for i in range(2,num):
#             L.append(L[i-1]+L[i-2])
#         self.names=L
#
#     def __str__(self):
#         return str(self.names)
#
#     def __len__(self):
#         return len(self.names)
#
# f = Fib(10)
# print(f)
# print(len(f))
class Solution:
    # array 二维列表
    def Find(self, target, array):
        for subarray in array:
            print(subarray)
            return target in subarray
        # write code here

a=Solution()
print(a.Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
