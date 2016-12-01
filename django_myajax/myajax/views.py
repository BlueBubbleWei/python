#!/usr/bin/python
#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

#load the first page
def index(request):
	return render(request,'index.html')

sign='Thanks for registering our website!'
def add(request):
	a=request.GET['a']
	b=request.GET['b']
	a=int(a)
	b=int(b)
	return HttpResponse(str(a+b))

def show(request):
	print request.POST
	ans=request.POST
	if request.method == 'POST':		
		name=request.POST['uname']
		#name=request.POST.get(u'uname')		
		pwd=request.POST.get(u"upass")
	return HttpResponse(str(name))
	#return response



