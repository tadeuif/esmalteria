from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse
from clientes.models import Cliente
from clientes.forms import ClienteForm
from agendamento.models import Agendamento
import datetime
from datetime import date

def index(request):
    context = {
        'title': 'LOGIN ESMALTERIA'
    }
    return render(request, "login.html", context)

def home(request):
    mydate = datetime.datetime.now()
    dia = date.today().day
    mes = date.today().month
    clientes2 = Cliente.objects.filter(dt_nascimento__day=dia, dt_nascimento__month=mes)
    agendamento = Agendamento.objects.filter(dt_agendamento__day=dia, dt_agendamento__month=mes)

    context = {'clientes':clientes2, 'mydate':mydate, 'agendamento':agendamento}
    return render(request,"home.html",context)

def teste(request):
    context = {
        'title': 'TESTE'
    }
    return render(request,"teste.html", context)

def login_redirect(request):
    return redirect('/accounts/login/')
    