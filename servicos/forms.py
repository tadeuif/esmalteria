from django import forms
from .models import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model =  Servico
        fields = ['nome','tipo','descricao','preco','produto','disponibilidade','tm_execucao']
        widgets = {
            'nome':forms.TextInput(attrs={'placeholder':'Informe o nome do serviço'}),
            'tipo':forms.TextInput(attrs={'placeholder':'Informe o tipo do serviço'}),
            'descricao':forms.TextInput(attrs={'placeholder':'Informe a descricao do serviço'}),
            'preco':forms.TextInput(attrs={'placeholder':'Informe o preço do serviço'}),
            'produto':forms.TextInput(attrs={'placeholder':'Informe o produto utilizado do serviço'}),
            'disponibilidade':forms.TextInput(attrs={'placeholder':'Informe se o serviço está disponível para venda'}),
            'tm_execucao':forms.TextInput(attrs={'placeholder':'Informe o tempo de execucao do serviço em minutos'})
        }