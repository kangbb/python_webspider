#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#学会并掌握在浏览器内查看源代码的方法
#exec(expression, [,globals[,locals]]
#[] 代表参数可选
#globals参数用来指定代码执行时可以使用的全局变量以及收集代码执行后的全局变量
#locals参数用来指定代码执行时可以使用的局部变量以及收集代码执行后的局部变量
#expression，为字符串，可以代表一个语句块；exec()函数可以执行它
#见：http://www.cnblogs.com/sesshoumaru/p/5998523.html

#关于变量作用域
#def 定义的函数内部的变量，只能该函数内部引用
#if/elif/else、try/except/finally、for/while函数块定义的变量，它隶属于的函数的任何地方可用

import urllib.request
import re
def getcontent(url, page):
	#模拟成浏览器
	headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/58.0.3029.96 Safari/537.36')
	#httphd = urllib.request.HTTPHandler(debuglevel = 1)
	#httpshd = urllib.request.HTTPSHandler(debuglevel = 1)
	#opener = urllib.request.build_opener(httphd, httpshd)
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]
	#将opener安装为全局
	urllib.request.install_opener(opener)
	data = urllib.request.urlopen(url).read().decode('utf-8')
	#构建对应用户提取的正则表达式 懒惰模式
	userpat = 'target="_blank" title="(.*?)">'
	#构建段子内容提取的正则表达式 懒惰模式
	contentpat = '<div class="content">\s*<span>(.*?)</span>\s*</div>'
	#寻找出所有的用户
	userlist=re.compile(userpat, re.S).findall(data) # re.S多行匹配
	#寻找出所有内容更
	contentlist = re.compile(contentpat, re.S).findall(data)
	x = 1
	#通过循环遍历所有段子内容并将内容分别赋给对应的变量
	for content in contentlist: 
		content = content.replace("\n", "")
		#用字符串作为变量名，先将对应字符串赋给一个变量
		name = "content"+str(x)
		#通过exec()函数实现用字符串作为变量名并赋值
		#先将name重命名为 "content"+str(x),再把content赋给这个变量
		exec(name+'=content')
		x += 1
	
	y = 1
	#通过for循环遍历用户，并输出该用户对应的内容
	for user in userlist:
		name = 'content'+str(y)
		print('用户'+str(page)+str(y)+'是：'+user)
		print('内容是:')
		#相当于执行了print(name)
		exec("print("+name+")")
		print("\n")
		y += 1

#分别获取各个页面的段子，通过for循环可以获取多页
for i in range(1,10):
	url = 'https://www.qiushibaike.com/8hr/page/'+str(i)
	getcontent(url, i)