from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
def index2(request2):
    return render(request2,'myfolder/index2.html')

def about(request):
    return render(request,'myfolder/about.html')

def register(request):
    return render(request,'myfolder/register.html')


# Create your views here.
