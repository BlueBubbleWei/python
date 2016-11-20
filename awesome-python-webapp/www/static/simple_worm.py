#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib
import webbrowser as web
url='http://163.com'
html=urllib.urlopen(url).read()
open('163.com.html','w').write(html)
web.open_new_tab('163.com.html')

