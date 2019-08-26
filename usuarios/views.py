from django.shortcuts import render,redirect,get_object_or_404
from usuarios.forms import RegistrationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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

    return render(request, 'usuarios/cadastrar_usuario.html', {'form': form}) #TESTE        
   
        


