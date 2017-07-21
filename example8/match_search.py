#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re
pattern = '.python.'
string = 'hellomypythonhistorython'
result1 = re.match(pattern,string)
result2 = re.search(pattern,string)
print(result1)
print(result2)