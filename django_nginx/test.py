#!/usr/bin/python
# -*- coding:utf-8 -*-

from django.conf import settings
from django.core.mail import EmailMultiAlternatives

try:
    print settings.DEFAULT_FROM_EMAIL
except Exception:
    print 'fail'
from_email=settings.DEFAULT_FROM_EMAIL
msg=EmailMultiAlternatives(subject,content,from_mail,[to_addr])
msg.content_subtype='html'

mssg.attach_file('./django_nginx.pdf')
msg.send





