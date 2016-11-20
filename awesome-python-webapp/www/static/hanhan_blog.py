#!/usr/bin/python
# -*- coding:utf-8 -*-
#str=r'<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102egl0.html">地震思考录</a>'
import urllib
url=urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html').read()
#print url
str=['']*50
title=url.find(r'<a title=')
href=url.find(r'href=',title)
html=url.find(r'.html',href)
con=url[href+6:html+5]
print con 

title=url.find(r'<a title=',html)                          
href=url.find(r'href=',title)                          
html=url.find(r'.html',href)                            
con=url[href+6:html+5]                              
print con

title=url.find(r'<a title=',html)     
href=url.find(r'href=',title) 
html=url.find(r'.html',href)                          
con=url[href+6:html+5]                                
print con  

i=0
while title!=-1 and href!=-1 and html!=-1 and i<50:
    title=url.find(r'<a title=',html)           
    href=url.find(r'href=',title)                                         
    html=url.find(r'.html',href)                                    
    con=url[href+6:html+5]                                      
    str[i]=con
    print str[i]

    i=i+1
else:
    print 'find  end'
#print the first page of all articles

j=0
while j<5'0:
    open(/article/)
