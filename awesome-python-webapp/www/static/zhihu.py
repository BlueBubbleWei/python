#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
#
import re

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
    print _xsrf
    return _xsrf[0]

get_xsrf()

