#!/usr/bin/python
# -*- coding:utf-8 -*-



#print (dir)
# print help(urllib.urlopen)
import urllib
url='http://www.baidu.com'
html=urllib.urlopen(url)

# check uurl
print html.geturl()


# if code !=200 webpage can't be used
code=html.getcode()
if code==200:
	print html.info()
	html= html.read()
else:
	print '404'




#if error in decode error
#html=html.decode('gbk').encode('utf-8')



# store html information
urllib.urlretrieve(url,"baidu.txt")
