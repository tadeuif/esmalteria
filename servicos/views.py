from django.shortcuts import render,redirect,get_object_or_404
from .models import Servico
from .forms import ServicoForm
from django.contrib import messages

def lista_de_servicos(request):
    servicos = Servico.objects.all().order_by('-id')
    return render(request,"servicos/lista_de_servicos.html",{'servicos':servicos})

def adicionar_servico(request):
    form = ServicoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = ServicoForm()
        messages.success(request,"Servico adicionado com sucesso")
        return redirect('lista_de_servicos')

    return render(request,"servicos/adicionar_servico.html",{'form':form})

def editar_servico(request,id=None):
    servico = get_object_or_404(Servico,id=id)
    form = ServicoForm(request.POST or None,instance=servico)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.info(request,"Servico editado com sucesso")
        return redirect('lista_de_servicos')
        
    return render(request,"servicos/editar_servico.html",{'form':form})

def remover_servico(request,id=None):
    servico = get_object_or_404(Servico,id=id)
    if request.method == "POST":
        servico.delete()
        messages.warning(request,"Servico removido com sucesso")
        return redirect('lista_de_servicos')

    return render(request,"servicos/remover_servico.html",{'servico':servico})
