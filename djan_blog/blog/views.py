from django.shortcuts import render
from django.http import HttpResponse

def home_views(request,*args,**kwargs):
    return render(request, "blog/home.html", context={}, status=200)


def about_views(request,*args,**kwargs):
    return render(request, "blog/about.html", context={}, status=200)