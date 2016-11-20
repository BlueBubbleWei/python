#!/usr/bin/python
# -*- coding:utf-8 -*-
#str=r'<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102egl0.html">地震思考录</a>'
import urllib
import time
page=1

url=urllib.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_'+str(page)+'.html').read()
#print url
str=['']*350
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


#open context for 1-7
while  page<=7:
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
    page=page+1
#print the first page of all articles
else :
    print page, 'all find end'
j=0
while j<350:
    print 'start:'
    content=urllib.urlopen(str[j]).read()
#    print str[j][-26:]
#    print content
    open(r'hanhan/'+str[j][-26:],'w+').write(content)
#    open(r'article/'+str[j][-26:],'w').write(content)
    print 'downloading',str[j]
    j=j+1
