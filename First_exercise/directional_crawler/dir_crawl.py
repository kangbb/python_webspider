#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import urllib.request
import http.cookiejar
import re

#设置视频编号
vid = '1773930974'
#设置评论起始编号
comid = "6294455663213585301"
#构造出真实评论请求的网址
url = "https://coral.qq.com/article/"+vid+"/comment?commentid="+comid+"&&reqnum=20"
#设置头信息伪装成浏览器爬取
headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
			"Connection":"keep-alive",
			"referer":"http://www.news.163.com/"}
#设置cookie
cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler({'http':'183.222.102.99:80'})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))
headall = []
for key,value in headers.items():
	item = (key,value)
	headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)
#构建函数，实现自动加载
def craw(vid, comid):
	url = "https://coral.qq.com/article/"+vid+"/comment?commentid="+comid+"&&reqnum=20"
	#爬取网页内容
	data = urllib.request.urlopen(url).read().decode('utf-8')
	return data
#构建正则表达式
idpat = '"id":"(.*?)"'
userpat = '"nick":"(.*?)"'
conpat = '"content":"(.*?)"'
#分别根据正则表达式查找所有的id\用户名\评论内容
#第一层，代表页数
for i in range(1,100):
	print('-----------------------------')
	print('第'+str(i)+'页评论内容')
	data = craw(vid, comid)
	#第二层循环代表评论，每页20条
	for j in range(0,20):
		idlist = re.compile(idpat,re.S).findall(data)
		conlist = re.compile(conpat,re.S).findall(data)
		userlist = re.compile(userpat,re.S).findall(data)
		#输出对应的信息，并对字符床进行unicode编码，使之正常显示
		print("用户名:"+eval('u"'+userlist[j]+'"'))
		print("评论内容:"+eval('u"'+conlist[j]+'"'))
		print("\n")
	#将最后一条信息的comid赋给该页的comid
	comid = idlist[19]