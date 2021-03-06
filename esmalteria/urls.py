"""esmalteria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from core.views import *
from django.conf.urls import url
from django.views.generic.base import TemplateView
from core.views import login_redirect, home
from usuarios.views import cadastrar, cadastrar_usuario, lista_de_usuarios
from produtos import views
from clientes import views
from usuarios import views
from servicos import views
from agendamento import views

urlpatterns = [
    url(r'^$', login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('', index, name="login"),
    path('home/', home, name='home'),
    path('clientes/',include('clientes.urls')), #ENDEREÇAR O PATH PARA LINK CLIENTES
    path('usuarios/',include('usuarios.urls')),
    path('usuarios/cadastrar_usuario',cadastrar_usuario,name='cadastrar_usuario'),
    path('usuarios/cadastrar_usuario/lista_de_usuarios',lista_de_usuarios,name='lista_de_usuarios'),
    path('produtos/', include('produtos.urls')),
    path('servicos/', include('servicos.urls')),
    path('agendamento/', include('agendamento.urls'))
]
