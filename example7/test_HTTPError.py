#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import urllib.request
import urllib.error

try:
	urllib.request.urlopen('http://blog.csdn.net')
except urllib.error.HTTPError as e:
	print(e.code)
	print(e.reason)