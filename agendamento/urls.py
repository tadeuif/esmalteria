from django.urls import path
from .views import lista_de_agendamento,adicionar_agendamento,editar_agendamento,remover_agendamento
urlpatterns = [
    path('',lista_de_agendamento,name='lista_de_agendamento'),
    path('adicionar_agendamento/',adicionar_agendamento,name='adicionar_agendamento'),
    path('agenda/editar_agendamento/<int:id>',editar_agendamento,name='editar_agendamento'),
    path('agenda/remover_agendamento/<int:id>',remover_agendamento,name='remover_agendamento')
    
]
