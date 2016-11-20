#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib

# taobao.com/robots.txt   forbid Baiduspider
# jd.com/robots.txt   all are forbidden  ,especially EtaoSpider
# specific content is denied
url=urllib.urlopen('http://blog.csdn.net/sunnyyoona/article/details/53244868')

print url.read()
print url.getcode()# code=403 forbbiden