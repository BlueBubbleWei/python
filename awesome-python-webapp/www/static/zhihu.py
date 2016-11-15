#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
#
import re

input=raw_input()

#user-agent
agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'

#header arguments
#'Host':'www.zhihu.com',	
#'Host':'static.zhihu.com',	
headers={
	'Host':'www.zhihu.com',	
	'Referer':'http://www.zhihu.com/',
	'User-Agent':agent,
}
session=requests.session()
#the function uses to get xsrf which is necessary for zhifu request
def get_xsrf():
	index_url='http://www.zhihu.com/'
	index_page=session.get(index_url,headers=headers)
	html=index_page.text
#	print html
	pattern=r'name="_xsrf" value="(.*?)"'
	_xsrf=re.findall(pattern,html)
#	print _xsrf
	return _xsrf[0]


def login(username,password):
#request way and url
	post_url='http://www.zhihu.com/login/phone_num'
#request data
	post_data={
		'_xsrf':get_xsrf(),
		'password':password,
		'remember_me':'true',
		'phone_num':username,
	}
	try:
		login_page=session.post(post_url,data=post_data,headers=headers)
		login_code=login_page.text
		print login_code
	except:
		print 'error'
if __name__=='__main__':
	username=input('please input your name:')
	password=input('please input your password:')
	login(username,password)
		
	
#get_xsrf()



