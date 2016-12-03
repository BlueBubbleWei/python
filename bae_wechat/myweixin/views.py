# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.template import loader, Context
from xml.etree import ElementTree as ET
import time
import hashlib

class WeChat(View):
  #这里我当时写成了防止跨站请求伪造，其实不是这样的，恰恰相反。因为django默认是开启了csrf防护中间件的
  #所以这里使用@csrf_exempt是单独为这个函数去掉这个防护功能。
  @csrf_exempt
  def dispatch(self, *args, **kwargs):
    return super(WeChat, self).dispatch(*args, **kwargs)
    
  def get(self, request):
  
    #下面这四个参数是在接入时，微信的服务器发送过来的参数
    signature = request.GET.get('signature', None)
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echostr = request.GET.get('echostr', None)
    
    #这个token是我们自己来定义的，并且这个要填写在开发文档中的Token的位置
    token = 'bubblefamily'
    
    #把token，timestamp, nonce放在一个序列中，并且按字符排序
    hashlist = [token, timestamp, nonce]
    hashlist.sort()
    
    #将上面的序列合成一个字符串
    hashstr = ''.join([s for s in hashlist])
    
    #通过python标准库中的sha1加密算法，处理上面的字符串，形成新的字符串。
    hashstr = hashlib.sha1(hashstr).hexdigest()
    
    #把我们生成的字符串和微信服务器发送过来的字符串比较，
    #如果相同，就把服务器发过来的echostr字符串返回去
    if hashstr == signature:
      return HttpResponse(echostr)









# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# from django.http.response import HttpResponse, HttpResponseBadRequest
# from django.views.decorators.csrf import csrf_exempt
# from wechat_sdk import WechatConf
# from wechat_sdk import WechatBasic
# from wechat_sdk.exceptions import ParseError
# from wechat_sdk.messages import (TextMessage, VoiceMessage, ImageMessage, VideoMessage, LinkMessage, LocationMessage, EventMessage, ShortVideoMessage)
# conf = WechatConf(
# 	token='bubblefamily',
# 	appid='wx2c7c822f57ee5d4c',
#    	appsecret='a6a846d1d632fd538e4966b40c9aa593 ',
#    	encrypt_mode='0',
#    	encoding_aes_key='dcC7n7ZB7shlbiQSGSBkVFdRsyfx4RKaqZQ4MghnK0G'
# )
# @csrf_exempt
# def wechat_home(request):
# 	signature = request.GET.get('signature')
# 	timestamp = request.GET.get('timestamp')
#    	nonce = request.GET.get('nonce')
#    	wechat_instance = WechatBasic(conf=conf)
# 	if not wechat_instance.check_signature(signature=signature,timestamp=timestamp,nonce=nonce):
# 		return HttpResponseBadRequest('Verify Failed')
# 	else:
# 		if 	request.method == 'GET':
# 			response = request.GET.get('echostr', 'error')
# 		else:
# 			try:
# 				wechat_instance.parse_data(request.body)    
# 				message = wechat_instance.get_message()            
# 				if isinstance(message, TextMessage):            
# 					reply_text = 'text'
# 				elif isinstance(message, VoiceMessage):            
# 					reply_text = 'voice'
# 				elif isinstance(message, ImageMessage):            
# 					reply_text = 'image'
# 				elif isinstance(message, LinkMessage):            
# 					reply_text = 'link'
# 				elif isinstance(message, LocationMessage):        
# 					reply_text = 'location'
# 				elif isinstance(message, VideoMessage):            
# 					reply_text = 'video'
# 				elif isinstance(message, ShortVideoMessage):    
# 					reply_text = 'shortvideo'
# 				else:
# 					reply_text = 'other'
# 				response = wechat_instance.response_text(content=reply_text)
# 			except ParseError:    
# 				return HttpResponseBadRequest('Invalid XML Data')
# 		return HttpResponse(response, content_type="application/xml")
 
