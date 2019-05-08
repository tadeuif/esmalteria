from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'LOGIN ESMALTERIA'
    }
    return render(request, "login.html", context)

def home(request):
    context = {
        'title': 'BEM VINDO'
    }
    return render(request, "home.html", context)

def teste(request):
    context = {
        'title': 'TESTE'
    }
    return render(request,"teste.html", context)