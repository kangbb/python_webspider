#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import threading
import queue
import re
import urllib.request
import time
import urllib.error

urlqueue = queue.Queue()
#模拟成为浏览器
headers = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/58.0.3029.96 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
listurl = []

#使用代理服务器的函数
def use_proxy(proxy_addr, url):
	#建立异常机制
	try:
		proxy = urllib.request.ProxyHandler( {'http':proxy_addr})
		opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
		# opener.addheaders = [headers]
		urllib.request.install_opener(opener)
		data = urllib.request.urlopen(url).read().decode('utf-8')
		return data
	except urllib.error.URLError as e:
		if hasattr(e, 'code'):
			print(e.code)
		if hasattr(e, 'reason'):
			print(e.reason)
		#若异常，延迟10秒执行
		time.sleep(10)
	except Exception as e:
		print("exception:"+str(e))
		#若异常，延迟1秒执行
		time.sleep(1)

#线程1，专门获取对应网址并处理为真实网址
class geturl(threading.Thread):
	def __init__(self, key, pagestart, pageend, proxy, urlqueue):
		threading.Thread.__init__(self)
		self.key = key
		self.pagestart = pagestart
		self.pageend = pageend
		self.proxy = proxy
		self.urlqueue = urlqueue
	def run(self):
		page = pagestart
		#编码关键词key
		keycode = urllib.request.quote(key)
		for page in range(self.pagestart, self.pageend+1):
			#分别构建各页的url链接，每次循环构建一次
			url = 'http://weixin.sogou.com/weixin?type=2&query='+keycode+'&page='+str(page)
			#用代理服务器爬取，解决IP被封问题
			data1 = use_proxy(proxy, url)
			# print(data1)
			#获取文章链接的正则表达式
			listurlpat = '<div class="txt-box">.*?(http://.*?)"'
			#获取每页的所有文章链接并添加到列表listurl
			listurl.append(re.compile(listurlpat, re.S).findall(data1))
		#便于调试
		print("共获取到"+str(len(listurl))+"页")
		for i in range(0, len(listurl)):
			#等待线程2，合理分配资源
			time.sleep(7)
			for j in range(0, len(listurl[j])):
				try:
					url=listurl[i][j]
					#处理成真实的url
					url=url.replace("amp;", "")
					print("第"+str(i)+"i"+str(j)+"j次入队")
					#把url放入队列
					self.urlqueue.put(url)
					#url入队完成
					self.urlqueue.task_done()
				except urllib.error.URLError as e:
					if hasattr(e, "code"):
						print(e.code)
					if hasattr(e, "reason"):
						print(e.reason)
					#若异常，延迟10秒执行
					time.sleep(10)
				except Exception as e:
					print("exception: " + str(e))
					#若异常，延迟1秒执行
					time.sleep(1)
					
#线程2，与线程1并行执行，从线程1提供的网址中依次爬取对应文章的信息并处理
class getcontent(threading.Thread):
	def __init__(self, urlqueue, proxy):
		threading.Thread.__init__(self)
		self.urlqueue = urlqueue
		self.proxy = proxy
	def run(self):
		#设置本地文件中的开始html编码
		html1 = '''<!DOCTYPE html PUBLIC "-// W3C// DTD XHML 1.0 Transitional// EN" "http://www.w3.org/TR/xhtml1/-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
<title>微信文章页面</title>
</head>
<body>'''
		fh = open("D:/Kangbb/python_webspider/First_exercise/multithread/1.html", "wb")
		fh.write(html1.encode("utf-8"))
		fh.close()
		fh=open("D:/Kangbb/python_webspider/First_exercise/multithread/1.html", "ab")
		i = 1
		while(True):
			try:
				#每次获得一个url
				url = self.urlqueue.get()
				#调用IP代理函数
				data = use_proxy(self.proxy, url)
				#文章标题的正则表达式
				titlepat = '<title>(.*?)</title>'
				#文章的正则表达式
				contentpat = 'id="js_content">(.*?id="js_sg_bar"'
				#通过对应正则表达式找到标题并赋给列表title
				title = re.compile(titlepat).findall(data)
				#通过正则表达式找到内容并赋给列表content
				content = re.compile(contentpat, re.S).findall(data)
				#初始化标题于内容
				thistitle = "此次没有获取到"
				thiscontent = "此次没有获取到"
				#如果标题列表不为空，说明找到了标题，取列表第零个元素，即此次标题赋给变量thistitle
				if title != []:
					thistitle = title[0]
				if content != []:
					thiscontent = content[0]
				#将标题和内容汇总，赋值给边个两dataall
				dataall = "</p>标题为："+thistitle+"</p><p>内容为:"+thiscontent+"</p><br>"
				#将篇文章的标题与内容的总信息写入对应文件
				fh.write(dataall.encode("utf-8"))
				print("第"+str(i)+"个网页处理") #便于调试
				i += 1
			except urllib.error.URLError as e:
				if hasattr(e, "code"):
					print(e.code)
				if hasattr(e, "reason"):
					print(e.reason)
				#若异常，延迟10秒执行
				time.sleep(10)
			except Exception as e:
				print("exception: " + str(e))
				#若异常，延迟1秒执行
				time.sleep(1)
		fh.close()
		#设置本地写入文件的html后缀
		html2 = '''</body>
</html>'''

#并行控制程序，若60秒未响应，并且存有url的队列已经空了，则判断执行成功
class control(threading.Thread):
	def __init__(self, urlqueue):
		threading.Thread.__init__(self)
		self.urlqueue = urlqueue
	def run(self):
		while(True):
			print('程序执行中')
			time.sleep(60)
			if self.urlqueue.empty():
				print('程序执行完毕')
				exit(0)

key = '人工智能'
proxy = '203.74.4.7:80'
proxy2 = '183.222.102.95:80'
pagestart = 1
pageend = 2
#创建线程1的对象并启动
t1 = geturl(key, pagestart, pageend, proxy, urlqueue)
t1.start()
#创建线程2的对象并启动
t2 = getcontent(urlqueue, proxy2)
t2.start()
#创建线程3的对象并启动
t3 = control(urlqueue)
t3.start()