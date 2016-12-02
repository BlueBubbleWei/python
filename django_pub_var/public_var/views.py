from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def index(request):
	return render(request,'index.html',{'info':'You will push into anonther wold.'})


def second(request):
	return render(request,'second.html')