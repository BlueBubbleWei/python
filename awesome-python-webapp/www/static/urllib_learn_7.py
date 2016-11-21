
#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib
from bs4 import BeautifulSoup

url="http://tieba.baidu.com/p/2772656630?fr_bdps_bottom_login=1"

def get_content(url):
	html=urllib.urlopen(url)
	content=html.read()
	html.close()
	return content

def get_img(info):
	
	# it recepts the content of html
	soup=BeautifulSoup(info)
	# dir used to check the class' functions
	#print dir(soup)
	#return type(soup)


	# <img class="BDE_Image"  class_='BDE_Image' save as key-value
	all_img=soup.find_all('img',class_='BDE_Image')
	#print all_img
	#return len(all_img)
	x=1
	for img in all_img:
		#print type(img)#<class 'bs4.element.Tag'>
		

		#the answer from next code----- http://imgsrc.baidu.com/forum/w%3D580/sign=6c193761c45c1038247ececa8210931c/ef01baa1cd11728bc259bb59cafcc3cec3fd2c51.jpg
		#print img['src']
		img_name='%s.jpg' %x
		#urllib.urlretrieve(img['src'],img_name)
		x=x+1


info = get_content(url)
print get_img(info)