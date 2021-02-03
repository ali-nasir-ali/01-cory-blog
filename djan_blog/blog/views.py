from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'auther': 'john',
        'title': ' blog post',
        'date_posted':'ugust 27,2019'
    },
    {
        'auther': 'mark',
        'title': ' blog st',
        'date_posted':'ugust 27,2029'
    }
]

def home_views(request,*args,**kwargs):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, "blog/home.html", context, status=200)


def about_views(request,*args,**kwargs):
    return render(request, "blog/about.html", {'title':'about'}, status=200)