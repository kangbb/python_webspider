#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import re
import urllib.request
import urllib.error

def craw(url, page):
	#httphd = urllib.request.HTTPHandler(debuglevel = 1)
	#httpshd = urllib.request.HTTPSHandler(debuglevel = 1)
	#opener = urllib.request.build_opener(httphd, httpshd)
	#urllib.request.install_opener(opener)
	html1 = urllib.request.urlopen(url).read() #读入的为二进制字节流
	html1 = str(html1) #转化为字符串
	part1 = '<div id="plist".+?<div class="page clearfix">' #注意书写，完全正确时，字符串为灰色
	# 实现全局匹配 返回所有匹配的结果
	result1 = re.compile(part1).findall(html1)
	# 把结果转换为字符串：
	result1 = result1[0]
	# 实现关于图片的正则表达式
	part2 = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
	imagelist = re.compile(part2).findall(result1)
	
	x = 1 # 记录图片顺序；当前图片无法爬取，则跳过
	for imageurl in imagelist:
		#j将图片存储到D:/Kangbb/python_webspider/First_exercise/picture_craw下，并以[页号+顺序号]命名
		imagename = "D:/Kangbb/python_webspider/First_exercise/picture_craw/"+str(page)+str(x)+".jpg"
		imageurl = "http://"+imageurl
		try:
			urllib.request.urlretrieve(imageurl, filename = imagename) # 将爬取的图片存储到本地
		except urllib.error.URLError as e:
			if hasattr(e, "code"):
				print("error")
				x += 1
			if hasattr(e, "reason"):
				print("error")
				x += 1
		x += 1

for i in range(1, 10):
	url = "http://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
	craw(url, i)