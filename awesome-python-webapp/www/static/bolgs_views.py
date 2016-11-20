#!/usr/bin/python
# -*- coding:utf-8 -*-
import webbrowser as web
import time
import os
import random
url='http://blog.csdn.net/weiyumeizi/article/details/53220828'
 
i=0
while i<4:
    web.open_new_tab(url)
    i=i+1
    time.sleep(0.8)
#   os.system('killall -9 firefox')  
else:
# close the brower
    os.system('kill all /F /IM firefox')

