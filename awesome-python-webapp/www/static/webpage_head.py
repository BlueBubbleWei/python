#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib
url='http://www.baidu.com'  #uth-8

#url='http://www.tudou.com'

#url='http://www.163.com'  #GBK

#url='http://www.taobao.com'

#url='http://movie.youku.com'

info=urllib.urlopen(url).info()

print info
print('--------------------')
# get the information of the head of the webpage
print info.getparam('charset')