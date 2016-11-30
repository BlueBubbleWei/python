from __future__ import unicode_literals   
from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def home(request):
    List=['Blue','Green','Yellow']
    Dict={'name':'BlueBubble','age':'24','sex':'female'}
    return render(request,'home.html',{
        'List':json.dumps(List),
        'Dict':json.dumps(Dict),
    })

