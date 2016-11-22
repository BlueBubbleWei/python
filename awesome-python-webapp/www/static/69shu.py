#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib
import re
import MySQLdb


def getList():
    html=urllib.urlopen('http://www.69shu.com/19251/').read()
    html=html.decode('gbk')
    html=html.encode('utf-8')
    #print html
    reg=r'<li><a href="(.*?)">(.*?)</a></li>'
    reg=re.compile(reg)
    text=re.findall(reg,html)[0]
    #print text
    #print html
    return text

def getContent(url):
    html=urllib.urlopen('http://www.69shu.com'+url).read()
    html=html.decode('gbk').encode('utf-8')
    return html
    #print html
#class Sql(object):

class Sql: 
    def __init__(self):
        conn=MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='noval',
        )

def insert(self,title,content):
        cur=self.conn.cursor()
        content=content.replace("'","\\'")
        cur.execute("insert into book values (null,'%s','%s')" %(titile,content))
        cur.close()
        sel.conn.commit()
mysql=Sql()
for i in getList():
    print i
    c_url=i[0]
    title=i[1]
    print c_url
    print title
    content=getContent(c_url)
    mysql.insert(title,content)
    print 'exexcuting title'
    print content
    break
mysql.close()
#getList()
