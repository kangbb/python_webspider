#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#开启DebugLog,程序边运行边打印调试日志
import urllib.request

httphd = urllib.request.HTTPHandler(debuglevel = 1)
httpshd = urllib.request.HTTPSHandler(debuglevel = 1)
opener = urllib.request.build_opener(httphd, httpshd)
#创建全局默认opener对象，在使用urlopener时，也是使用我们安装的opener对象
urllib.request.install_opener(opener)

data = urllib.request.urlopen('http://edu.51cto.com')