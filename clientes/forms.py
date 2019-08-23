from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model =  Cliente
        fields = ['nome','email','cpf','celular','redes']
        widgets = {
            'nome':forms.TextInput(attrs={'placeholder':'Informe o nome do cliente'}),
            'email':forms.TextInput(attrs={'placeholder':'Informe o email do cliente'}),
            'cpf':forms.TextInput(attrs={'placeholder':'Informe o cpf do cliente'}),
            'celular':forms.TextInput(attrs={'placeholder':'Informe o celular do cliente'}),
            'redes':forms.TextInput(attrs={'placeholder':'Informe a rede social do cliente'})
        }