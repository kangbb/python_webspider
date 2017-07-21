#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#关于 compile()函数和findall()函数，
#参考网址：http://blog.csdn.net/drdairen/article/details/51134816

#python:字符串转换成字节的三种方式 
#str='zifuchuang'
#第一种 b'zifuchuang'
#第二种bytes('zifuchuang',encoding='utf-8')
#第三种('zifuchuang').encode('utf-8')
import re
import urllib.request
def getlink(url):
	#模拟成浏览器
	headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/58.0.3029.96 Safari/537.36')
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]
	#将opener安装为全局
	urllib.request.install_opener(opener)
	file = urllib.request.urlopen(url).read()
	data = str(file)
	
	pattern = '(https?://[^\s)";]+\.(\w|/)*)'
	link = re.compile(pattern).findall(data) # 函数返回一个包含二元tuple元素的list
	#去除重复元素
	link = list(set(link))# set()可以去除重复；list()将set转换为list
	return link

url = "http://blog.csdn.net/"
linklist = getlink(url)
for link in linklist:
	print(link[0])
	fhandle = open('D:/Kangbb/python_webspider/First_exercise/link_craw/1.txt', 'ab')
	fhandle.write((link[0]).encode('utf-8'))
	fhandle.write(b'\n')
	fhandle.close()