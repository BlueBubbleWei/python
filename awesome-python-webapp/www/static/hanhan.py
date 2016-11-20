#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib  
import time  
page=1  
while page<=7:  
    url=['']*50      #新浪播客每页显示50篇  
    temp='http://blog.sina.com.cn/s/articlelist_1191258123_0_'+str(page)+'.html'  
    con =urllib.urlopen(temp).read()  
    #初始化  
    i=0  
    title=con.find(r'<a title=')  
    href=con.find(r'href=',title)  
    html = con.find(r'.html',href)  
    #循环显示文章  
    while title!=-1 and href!=-1 and html!=-1 and i<50:  
        url[i]=con[href+6:html+5]  
        print url[i] #显示文章URL  
        #下面的从第一篇结束位置开始查找  
        title=con.find(r'<a title=',html)  
        href=con.find(r'href=',title)  
        html = con.find(r'.html',href)  
        i=i+1  
    else:
        print 'end page=',page  
        #下载获取文章  
    j=0  
    while(j<i):        #前面6页为50篇 最后一页为i篇  
        content=urllib.urlopen(url[j]).read()  
        open(r'hanhan/'+url[j][-26:],'w+').write(content) #写方式打开 +表示没有即创建  
        j=j+1  
        time.sleep(1)  
    else:  
        print 'download'  
        page=page+1  
else:  
    print 'all find end'  
