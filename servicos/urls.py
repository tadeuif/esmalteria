from django.urls import path
from .views import lista_de_servicos,adicionar_servico,editar_servico,remover_servico
urlpatterns = [
    path('',lista_de_servicos,name='lista_de_servicos'),
    path('adicionar_servico/',adicionar_servico,name='adicionar_servico'),
    path('servicos/editar_servico/<int:id>',editar_servico,name='editar_servico'),
    path('servicos/remover_servico/<int:id>',remover_servico,name='remover_servico')
    
]
