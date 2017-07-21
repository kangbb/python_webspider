#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import urllib.request

# 爬取百度的内容并保存
file = urllib.request.urlopen('http://www.baidu.com')
data = file.read()
# print(data)

fhandle = open('D:/Kangbb/python_webspider/example1/1.html', 'wb')
fhandle.write(data)
fhandle.close()

# 使用urllib.request.urlretrieve(url,filename = 本地文件地址),爬取并直接保存
# urllib.request.urlcleanup()清除缓存
filename = urllib.request.urlretrieve('http://edu.51cto.com', filename = 'D:\Kangbb\python_webspider\example1/2.html')
urllib.request.urlcleanup()

# 返回当前环境相关信息 file.info()
print('当前环境相关信息:\n', file.info())

# 获取当前爬取网页的状态 getcode()
if file.getcode() == 200:
	print('爬取百度主页响应正确,网址为：', file.geturl())
else:
	print('爬取百度主页响应错误')

# 对网址编码，解码,主要针对不和规范的url地址
print('\n\n对网址编码，解码:')
print('http：//www.baidu.com  ', urllib.request.quote('http：//www.baidu.com'))
print('http%3A//www.sina.com.cn  ', urllib.request.unquote('http%3A//www.sina.com.cn'))
