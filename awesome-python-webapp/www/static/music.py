#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import web
urls=(
    '/','Index',#it's moren
    '/2.php','Php',
    '/s','So'
)

render=web.template.render('templates')


def getUrl(name):
    html=urllib.urlopen('http://s.music.163.com/search/get/?type=1&s=%s&limit=1' %name).read()   
    js_html=json.loads(html)# change json into dict
    



class Index:
    def Get(self):# it also means that Get is the way webpage request
        return 'Hello world'

class Php:
    def Get(self):
        return '2.php'


class So:
    def Get(self):
        i=web.inpue()
        name=i.get('name')
        urllib.urlopen('http://s.music.163.com/search/get/?type=1&s=%s&limit=1' %name).read()
        return '<hl>%s</h1>' %name
if __name__ =='__main__':
    app.web.App()
    app.MainLoop()
