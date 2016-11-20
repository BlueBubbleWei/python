#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import random


url='http://blog.csdn.net/sunnyyoona/article/details/53244868'
my_headers=[
]

def get_content(url,headers):
	"""
	put the page you want
	"""
	random_header=random.choice(headers)
	req=