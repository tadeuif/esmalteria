from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse


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

def login_redirect(request):
    return redirect('/accounts/login/')
    