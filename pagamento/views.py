from django.shortcuts import render,redirect,get_object_or_404
from .models import Pagamento
from .forms import PagamentoForm
from django.contrib import messages

def lista_de_pagamento(request):
    pagamento = Pagamento.objects.all().order_by('-id')
    return render(request,"pagamento/lista_de_pagamento.html",{'pagamento':pagamento})

def adicionar_pagamento(request):
    form = PagamentoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = PagamentoForm()
        messages.success(request,"Pagamento adicionado com sucesso")
        return redirect('lista_de_pagamento')

    return render(request,"pagamento/adicionar_pagamento.html",{'form':form})

def editar_pagamento(request,id=None):
    pagamento = get_object_or_404(Pagamento,id=id)
    form = PagamentoForm(request.POST or None,instance=pagamento)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.info(request,"Pagamento editado com sucesso")
        return redirect('lista_de_pagamento')
        
    return render(request,"pagamento/editar_pagamento.html",{'form':form})

def remover_pagamento(request,id=None):
    pagamento = get_object_or_404(Pagamento,id=id)
    if request.method == "POST":
        pagamento.delete()
        messages.warning(request,"Pagamento removido com sucesso")
        return redirect('lista_de_pagamento')

    return render(request,"pagamento/remover_pagamento.html",{'pagamento':pagamento})
