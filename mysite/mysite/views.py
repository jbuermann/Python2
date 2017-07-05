from django.shortcuts import render

def home(request):
    return render(request,"home.html",{'hello' : "Welcome"})


def article(request):
    return render(request,"home.html",{'hello' : "Article"})