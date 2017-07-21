#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import http.cookiejar #导入cookie处理模块

url = "http://bbs.chinaunix.net/member.php?mod=\
logging&action=login&loginsubmit=\
yes&loginhash=LtiFI"

postdata = urllib.parse.urlencode({ #需要输入自己的用户名、密码
	'username': 'Kiloveyousmile',
	'password': 'zhang7758521tm'
}).encode('utf-8') #使用urlencode编码处理后，再设置为utf-8编码
req = urllib.request.Request(url, postdata) #构建Request对象
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
		AppleWebKit/537.36 (KHTML, like Gecko) \
		Chrome/58.0.3029.96 Safari/537.36')
##使用HTTPCookiejar.CookieJar()创建CookieJar对象
cjar = http.cookiejar.CookieJar()
##使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
#将opener安装为全局
urllib.request.install_opener(opener)
file = opener.open(req)
data = file.read() #登陆并爬取对应网页
fhandle = open('D:\Kangbb\python_webspider\example8/1.html', 'wb')
fhandle.write(data)
fhandle.close()

url2 = "http://bbs.chinaunix.net/"
data2 = urllib.request.urlopen(url2).read() #爬取该站下的其他网页
fhandle = open('D:\Kangbb\python_webspider\example8/2.html', 'wb')
fhandle.write(data2)
fhandle.close()
