from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class MyView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse('Hello,world!')

