#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from  .models import Column,Article
# Create your views here.

def index(request):
	time = getTime()
	count = getCount()
	home_display_columns=Column.objects.filter(home_display=False)
	nav_display_columns=Column.objects.filter(nav_display=False)
	print home_display_columns
	print nav_display_columns
	return render(request,'index.html',{
		'home_display_columns':home_display_columns,
		'nav_display_columns':nav_display_columns, 
		"count":count,
		"time":time
		})
	# columns=Column.objects.all()
	# # return HttpResponse(u'Welcome Here!')
	# print columns
	# return render(request,'index.html',{'columns':columns})


def column_detail(request,column_slug):
	#should it need to import models.py
	column=Column.objects.get(slug=column_slug)
	# return HttpResponse('column_slug:'+column_slug)
	return render(request,'news/column.html',{'column':column})


def article_detail(request,pk,article_slug):
	article=Article.objects.get(pk=pk)
	# article=Article.objects.filter(slug=article_slug)[0]
	# article=Article.objects.get(slug=article_slug)
	# return HttpResponse('article_slug:'+article_slug)
	if article_slug !=article_slug:
		return redirect(article,permanent=True)
	return render(request,'news/article.html',{'article':article})




def getTime():#获取当前时间
    import time
    return time.ctime()

def getCount():#获取访问次数
    countfile  = open('count.dat','a+')#以读写形式打开记录计数的文件
    counttext = countfile.read()   
    try:
        count = int(counttext)+1
    except:
        count = 1    
    countfile.seek(0)
    countfile.truncate()#清空文件
    countfile.write(str(count))#重新写入新的访问量
    countfile.flush()
    countfile.close()
    return count
