#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#匹配.com或.cn后缀的URL网址
import re

pattern = '[a-zA-Z]+://[\S]*[.com|.cn]' # 或 '[a-zA-Z]+://[^\s]*[.com|.cn]'
string = "<a herf='http://www.baidu.com'>百度首页</a>"
result = re.search(pattern, string)
print(result)
