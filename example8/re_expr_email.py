#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#匹配电话号码
import re

pattern = '\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*'
string = "<a jerf='http://www.baidu.com'>百度首页</a><br><a herf='mailto:c-e+o@iqi-anyue.com.cn'>"
result = re.search(pattern, string)
print(result)
