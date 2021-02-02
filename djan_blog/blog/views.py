from django.shortcuts import render
from django.http import HttpResponse

def home(request,*args,**kwargs):
    return HttpResponse('<h1> hello world </h1>')
    #return render(request, "pages/home.html", context={}, status=200)
