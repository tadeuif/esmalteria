from django.shortcuts import render,redirect,get_object_or_404
from usuarios.forms import RegistrationForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def cadastrar(request):
    return render(request, "usuarios/cadastrar_usuario.html")

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Usuário adicionado com sucesso")
            return redirect('cadastrar_usuario')
        
        else:
            form = RegistrationForm()

            args = {'form': form}
            return render(request, 'cadastrar_usuario.html', args)


