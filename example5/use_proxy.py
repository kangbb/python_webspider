#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import urllib.request
#使用代理服务器爬取网站内容

def use_proxy(proxy_addr,request):
	# import import urllib.request
	proxy = urllib.request.ProxyHandler({ 'http':proxy_addr})
	opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
	urllib.request.install_opener(opener)
	data = urllib.request.urlopen(req).read()
	return data

try:
	proxy_addr = '115.46.156.175:8123'
	req = urllib.request.Request('http://www.baidu.com')
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
		AppleWebKit/537.36 (KHTML, like Gecko) \
		Chrome/58.0.3029.96 Safari/537.36')
	data = use_proxy(proxy_addr, req)
except Exception as e:
	print('Error-->', str(e))
finally:
	print(len(data))
	fhandle = open('D:\Kangbb\python_webspider\example5/1.html', 'wb')
	fhandle.write(data)
	fhandle.close()

	
