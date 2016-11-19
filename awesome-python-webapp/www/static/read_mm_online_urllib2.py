#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib
import urllib2
mmurl="http://mm.taobao.com/json/request_top_list.htm?type=0&page="
i=0

while i<4:
    #html=urllib2.urlopen('https://mm.taobao.com/json/request_top_list.htm?type=0&page=')
    html=mmurl+str(i)
    #print html
    html=urllib2.urlopen(html).read()
    #print html 
    head="<img src="
    tail=".jpg"
    #picture url starts and ends
    pichead=html.find(head)
    picend=html.find(tail)
    #find index and offsets
    # the picture url
    #print "http:"+ html[pichead+len(head):picend+len(tail)]
    print '-----------------'
    ahead=r'<a class="lady-name" href'
    atail="target"
    ahead_index=html.find(ahead)
    atail=html.find(atail,ahead_index)
    #print atail
    final= "http:"+html[ahead_index+len(ahead)+2:atail-2]
    print final
    modelurl=urllib2.urlopen(final)
    murl=modelurl.read()
    # print personal homepage
    #print murl
    print '--------------'
    imgh=r' id="J_MmPheader" src='
    imge=".jpg"
    iph=murl.find(imgh)
    #find imge in the search result of iph
    ipe=murl.find(imge,iph)
    personal_pic='http:'+ murl[iph+len(imgh)+1:ipe+len(imge)].strip()
    #print personal_pic
    urllib.urlretrieve(personal_pic,'img/a'+str(i)+".jpg")
    i=i+1
