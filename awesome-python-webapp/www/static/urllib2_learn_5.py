#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib2

# Request Headers is necessary for Host,Referer(current webpage),User-Agent


url='http://blog.csdn.net/sunnyyoona/article/details/53244868'


# the following is necessary for pretending as a web browser
# req=urllib2.Request(url)
# req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36")

# req.add_header("GET",url)
# req.add_header("Host","blog.csdn.net")
# req.add_header("Referer","http://blog.csdn.net/sunnyyoona/article/details/53244868")

my_headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
	"Host":"blog.csdn.net",
	"Referer":"http://blog.csdn.net/sunnyyoona/article/details/53244868",
	"GET":url,
}
req=urllib2.Request(url,headers=my_headers)





html=urllib2.urlopen(req) #the concret content is denied
print html.read()
#print req.headers.items