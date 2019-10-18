from django.shortcuts import render,redirect,get_object_or_404
from usuarios.forms import RegistrationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
import django.db

def cadastrar(request):
    return render(request, 'usuarios/cadastrar_usuario.html')

def cadastrar_usuario(request):
    if not request.method == 'POST':
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'usuarios/cadastrar_usuario.html', context)

    form = RegistrationForm(request.POST)

    if form.is_valid():
        form = RegistrationForm(request.POST)
        form.save()
        #context = {'form': form}
        messages.success(request,"Usuário adicionado com sucesso")
        return HttpResponseRedirect('cadastrar_usuario', {'form': form})

    return render(request, 'usuarios/cadastrar_usuario.html', {'form': form})      
   
def lista_de_usuarios(request):
    usuarios_query = User.objects.all()
    usuarios = {'usuarios': usuarios_query}
    return render(request, 'usuarios/lista_de_usuarios.html', usuarios)        


