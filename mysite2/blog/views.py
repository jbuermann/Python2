from django.shortcuts import render
from .models import *


def index(request):
    return render(request,"blog/home.html",{'hello' : "Howdy Blogger"})


def articles(request):
    p = post.objects.filter(type=2)
    params = [];
    for i in p:
        params.append({'title' : i.title,'url' : i.alias})
    return render(request,"blog/articles.html",{'data' : params})


def article(request,alias):
    p = post.objects.get(alias=alias, type='2')

    params = {
                'title': p.title,
                'author': p.author,
                'timestamp': p.timestamp,
                'body': p.body
            }
    return render(request, "blog/article.html", {'data' : params})
