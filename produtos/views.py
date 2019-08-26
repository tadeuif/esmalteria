from django.shortcuts import render,redirect,get_object_or_404
from .models import Produto
from .forms import ProdutoForm
from django.contrib import messages

def lista_de_produtos(request):
    produtos = Produto.objects.all().order_by('-id')
    return render(request,"produtos/lista_de_produtos.html",{'produtos':produtos})

def adicionar_produto(request):
    form = ProdutoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        form = ProdutoForm()
        messages.success(request,"Produto adicionado com sucesso")
        return redirect('lista_de_produtos')

    return render(request,"produtos/adicionar_produto.html",{'form':form})

def editar_produto(request,id=None):
    produto = get_object_or_404(Produto,id=id)
    form = ProdutoForm(request.POST or None,instance=produto)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.info(request,"Produto editado com sucesso")
        return redirect('lista_de_produtos')
        
    return render(request,"produtos/editar_produto.html",{'form':form})

def remover_produto(request,id=None):
    produto = get_object_or_404(Produto,id=id)
    if request.method == "POST":
        produto.delete()
        messages.warning(request,"Produto removido com sucesso")
        return redirect('lista_de_produtos')

    return render(request,"produtos/remover_produto.html",{'produto':produto})
