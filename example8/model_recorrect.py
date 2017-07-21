#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re
pattern1 = 'python'
pattern2 = 'python'
string = 'abcdfphp345Pythony_py'
result1 = re.search(pattern1,string)
result2 = re.search(pattern2,string, re.I)
print(result1)
print(result2)