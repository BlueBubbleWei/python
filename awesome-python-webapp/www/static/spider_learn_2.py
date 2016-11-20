#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib

def callback(*a):
	print a




url="http://baidu.com"
local='/root/Documents/mygit/python/awesome-python-webapp/www/static/spider_learn_1.py'
urllib.urlretrieve(url,local,callback)
print urllib.urlopen(url).info()