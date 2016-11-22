# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#def index(request):
#   return HttpResponse('<h1>Hello,world!</h1>')


def index(request):
    return render(request,'home.html')

def add(request):
    a=request.GET['a']
    b=request.GET['b']
    c=int(a)+int(b)
    return HttpResponse(str(c))


def add2(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))


def old_add2_redirect(request,a,b):
    return HttpResponseRedirect(
        reverse('add2',args=(a,b))
    )
