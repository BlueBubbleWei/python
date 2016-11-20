#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib
import chardet

# url='http://www.baidu.com'
# url='http://www.jd.com'
# content=urllib.urlopen(url).read()


# # check the content of the webpage if it is utf-8
# print chardet.detect(content)# the type of returned value is dict

#-------------------------------------------


# traversing the list is not in order
def auto_detect(url):
	content=urllib.urlopen(url).read()
	result=chardet.detect(content)
	encoding=result['encoding']
	return encoding


urls={
	'http://www.baidu.com',
	'http://www.163.com',
	'http://www.taobao.com',
	'http://www.jd.com',
	'http://www.dangdang.com',
}

for i in urls:
	print i,auto_detect(i)
	
