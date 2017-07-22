#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import threading
class A(threading.Thread):
	def __init__(self):
		#初始化该线程
		threading.Thread.__init__(self)
	def run(self):
		#执行该线程的内容
		for i in range(10):
			print("我是线程A")
class B(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		#执行该线程的内容
		for i in range(10):
			print("我是线程B")
#实例化线程A为t1
t1 = A()
#启动线程t1
t1.start()
#实例化线程A为t2
t2 = B()
#启动线程t2,与t1同时执行
t2.start()