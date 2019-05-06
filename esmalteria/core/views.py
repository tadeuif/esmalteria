from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'LOGIN ESMALTERIA'
    }
    return render(request, "login.html", context)