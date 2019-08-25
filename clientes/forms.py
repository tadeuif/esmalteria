from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model =  Cliente
        fields = ['nome','sobrenome','email','cpf','dt_nascimento','celular','redes']
        widgets = {
            'nome':forms.TextInput(attrs={'placeholder':'Informe o nome do cliente'}),
            'sobrenome':forms.TextInput(attrs={'placeholder':'Informe o sobrenome do cliente'}),
            'email':forms.TextInput(attrs={'placeholder':'Informe o email do cliente'}),
            'cpf':forms.TextInput(attrs={'placeholder':'Informe o cpf do cliente'}),
            'dt_nascimento':forms.TextInput(attrs={'placeholder':'Informe a data de nascimento do cliente'}),
            'celular':forms.TextInput(attrs={'placeholder':'Informe o celular do cliente'}),
            'redes':forms.TextInput(attrs={'placeholder':'Informe a rede social do cliente'})
        }