from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def home(request):
# send a string to template home.html
    string="summer is coming to a close,dreaming is over once again."
#    TutorialLists = ["HTML", "CSS", "jQuery", "Python", "Django"]
#    info_dict = {'name':'Blue','age':'25','sex':'female'}
#   return render(request, 'home.html', {'TutorialLists':TutorialLists}) 
#    return render(request, 'home.html', {'info_dict':info_dict})
    list=map(str,range(100))
    value=75
    return render(request,'home.html',{'List':list,'string':string,'value':value})
def add(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))


def out_val(request,value):
    value=int(value)
    return HttpResponse(request,'home.html',{"value":value})  
