#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#使得爬虫模拟成为浏览器--Headers属性
#爬取一些无法爬取的网页
#使用 add_header 方法
import urllib.request

url = 'http://blog.csdn.net/kiloveyousmile/article/details/74318440'
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/58.0.3029.96 Safari/537.36') #使用该函添加报头信息

data = urllib.request.urlopen(req).read() # 读取网站信息
fhandle = open('D:\Kangbb\python_webspider\example2/2.html', 'wb')
fhandle.write(data)
fhandle.close()