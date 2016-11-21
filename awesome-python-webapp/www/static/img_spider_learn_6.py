#!/usr/bin/python
# -*- coding:utf-8 -*-

import re
import urllib
import time

url="http://tieba.baidu.com/p/2772656630?fr_bdps_bottom_login=1"

def get_content(url):
	html=urllib.urlopen(url)
	content=html.read()
	html.close()
	return content



def get_img(info):
	#  . macth any signal except space 
	# + try to get as short times as possible
	
	# (.+?\.jpg) is exactly what you want
	regex=r'class="BDE_Image" src="(.+?\.jpg)"'
	pat=re.compile(regex)

	images_code=re.findall(pat,info)
	#print images_code
	i=0
	for image_url in images_code:
		#image_url=list(image_url)[len(r)]
		print  image_url
		#urlretrive will save file to local
		time.sleep(2)
		urllib.urlretrieve(image_url,"%s.jpg" %i)
		i=i+1


info=get_content(url)S
print get_img(info)

	#pass
	