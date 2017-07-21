#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re # 导入模块

pattern = 'yue' # 原子
string = 'http://yum.iqianyue.com'
result1 = re.search(pattern, string)
print(result1)