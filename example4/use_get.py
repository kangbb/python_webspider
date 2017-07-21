#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#构造get请求，爬取检索网页
#一般形式 http://网址/?字段名1=字段内容1&字段名2=字段内容2   可有多个字段名
#使用urllib.request.quote()进行编码

import urllib.request
keywd = 'hello'
keywd_code = urllib.request.quote(keywd) 
url = 'http://www.baidu.com/s?wd=' + keywd_code
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
	AppleWebKit/537.36 (KHTML, like Gecko) \
	Chrome/58.0.3029.96 Safari/537.36')
data = urllib.request.urlopen(req).read()
fhandle = open('D:\Kangbb\python_webspider\example4/1.html', 'wb')
fhandle.write(data)
fhandle.close()