from django.urls import path
from .views import cadastrar_usuario, cadastrar
urlpatterns = [
    path('',cadastrar_usuario,name='cadastrar_usuario'),
    
]
