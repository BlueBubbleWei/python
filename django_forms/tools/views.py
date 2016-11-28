from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm
# Create your views here.

# def index(request):
#     return render(request,'index.html')

def add(request):
    a=request.GET['a']
    b=request.GET['b']
    a=int(a)
    b=int(b)
    return HttpResponse(str(a+b))

def index(request):
	#when submit forms
	if request.method == 'POST':
		form=AddForm(request.POST)
		if form.is_valid():
			a=form.cleaned_data['a']
			b=form.cleaned_data['b']
			return HttpResponse(str(int(a)+int(b)))
	else:
		form=AddForm()
		return render(request,'index.html',{'form':form})