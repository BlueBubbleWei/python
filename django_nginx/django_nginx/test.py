#!/usr/bin/python
# -*- coding:utf-8 -*-

from django.conf import settings
#from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail

send_mail('Subject here', 'Here is the message.', 'from@278663275@qq.com',
    ['to@278663275@qq.com'], fail_silently=False)

try:
    print settings.DEFAULT_FROM_EMAIL
except Exception:
    print 'fail'
#from_email=settings.DEFAULT_FROM_EMAIL
#msg=EmailMultiAlternatives(subject,content,from_mail,[to_addr])
#msg.content_subtype='html'

#msg.send





