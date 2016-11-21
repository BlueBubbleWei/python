#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import random


url='http://blog.csdn.net/sunnyyoona/article/details/53244868'
my_headers=[
	"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36 QIHU 360SE",
]

def get_content(url,headers):
	"""
	put the 403 page you want
	"""

	# avoid the website stop your spider you have to change your user-agent usually
	random_header=random.choice(headers)
	#print random_header
#----------------------------------------

	req=urllib2.Request(url)
	req.add_header("User-Agent",random_header)
	req.add_header("Host","blog.csdn.net")
	req.add_header("Referer","Referer:http://m.blog.csdn.net/article/details?id=53244868")
	req.add_header("Get",url)
	content=urllib2.urlopen(req).read()
	#return content


print get_content(url,my_headers)