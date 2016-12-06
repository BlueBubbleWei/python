# coding: UTF-8
import os

import sae
import web
import sys


urls = (
'/wechat','wechatInterface',

)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
sys.path.insert(0, os.path.join(app_root, 'site-packages')) 
render = web.template.render(templates_root)

from WechatInterface import wechatInterface

app = web.application(urls, globals()).wsgifunc()      
application = sae.create_wsgi_app(app)




