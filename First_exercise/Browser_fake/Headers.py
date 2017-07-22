import urllib.request
import http.cookiejar

url = "http://news.163.com/17/0721/20/CPT622E2000189FH.html"
#以dict形式设置headers头信息
headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
			"Connection":"keep-alive",
			"referer":"http://www.news.163.com/"}
#Accept-Encoding: gzip, deflate一般不添加，因为需要解码

#设置cookie
cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler({'http':'127.0.0.1:8888'})
#proxy参数可选，也可以设置为其他值
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))
#建立空列表，为了以指定格式存储头信息
headall = []
#通过for循环遍历字典，构造除指定格式的headers信息
for key,value in headers.items():
	item = (key,value)
	headall.append(item)
#将指定格式的headers信息添加好
opener.addheaders = headall
#将opener安装为全局
urllib.request.install_opener(opener)

#简单测试代码
data = urllib.request.urlopen(url).read()
fhandle = open("D:/Kangbb/python_webspider/First_exercise/Browser_fake/1.html", "wb")
fhandle.write(data)
fhandle.close()