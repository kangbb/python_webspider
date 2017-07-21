#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#匹配电话号码
import re

pattern = '\d{3}-\d{8}|\d{4}-\d{7}'
string = '134-5779965324524-425345435'
result = re.search(pattern, string)
print(result)
