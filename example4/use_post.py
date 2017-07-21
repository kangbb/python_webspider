#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#在注册、登陆等操作时，会遇到
#构造post请求，步骤：
#1）设置url网址
#2）构建表单数据，用urllib.parse.urlrncode对数据编码
#3）创建Request对象，参数包括URL地址和要传递的数据
#4）使用add_header添加http报头信息’
#5）使用urllib.request.urlopen()打开Reqest对象
#6）后续处理

import urllib.request
import urllib.parse #对数据编码
url = 'http://www.iqianyue.com/mypost/'
postdata = urllib.parse.urlencode({
	'name': 'ceo@iqianyue.com',
	'pass': 'aA123456'
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
	AppleWebKit/537.36 (KHTML, like Gecko) \
	Chrome/58.0.3029.96 Safari/537.36') #使用该函添加报头信息
data = urllib.request.urlopen(req).read() # 读取网站信息
fhandle = open('D:\Kangbb\python_webspider\example4/2.html', 'wb')
fhandle.write(data)
fhandle.close()	