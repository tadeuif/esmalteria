from django.shortcuts import render,redirect,get_object_or_404
from .models import Agendamento
from .forms import AgendamentoForm
from django.contrib import messages

def lista_de_agendamento(request):
    agendamento = Agendamento.objects.all().order_by('-id')
    return render(request,"agenda/lista_de_agendamento.html",{'agendamento':Agendamento})

def adicionar_agendamento(request):
    form = AgendamentoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = AgendamentoForm()
        messages.success(request,"Agendado com sucesso")
        return redirect('lista_de_agendamentos')

    return render(request,"agenda/adicionar_agendamento.html",{'form':form})

def editar_agendamento(request,id=None):
    agendamento = get_object_or_404(Agendamento,id=id)
    form = AgendamentoForm(request.POST or None,instance=agendamento)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.info(request,"Agendamento editado com sucesso")
        return redirect('lista_de_agendamentos')
        
    return render(request,"agenda/editar_agendamento.html",{'form':form})

def remover_agendamento(request,id=None):
    agendamento = get_object_or_404(Agendamento,id=id)
    if request.method == "POST":
        agendamento.delete()
        messages.warning(request,"Agendamento removido com sucesso")
        return redirect('lista_de_agendamentos')

    return render(request,"agenda/remover_agendamento.html",{'agendamento':Agendamento})
