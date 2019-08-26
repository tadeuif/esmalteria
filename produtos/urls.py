from django.urls import path
from .views import lista_de_produtos,adicionar_produto,editar_produto,remover_produto
urlpatterns = [
    path('',lista_de_produtos,name='lista_de_produtos'),
    path('adicionar_produto/',adicionar_produto,name='adicionar_produto'),
    path('produtos/editar_produto/<int:id>',editar_produto,name='editar_produto'),
    path('produtos/remover_produto/<int:id>',remover_produto,name='remover_produto')
    
]
