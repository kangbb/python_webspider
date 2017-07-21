#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re
pattern = '.python.'
string = 'hellomypythonhistorypythonym'
result1 = re.sub(pattern,'php', string)
result2 = re.sub(pattern,'php', string, 1)
print(result1)
print(result2)