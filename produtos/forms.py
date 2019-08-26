from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model =  Produto
        fields = ['nome','tipo','marca','cor','qtd_disponivel','qtd_min_disponivel','pco_custo','pco_venda','dt_ultima_compra']
        widgets = {
            'nome':forms.TextInput(attrs={'placeholder':'Informe o nome do produto'}),
            'tipo':forms.TextInput(attrs={'placeholder':'Informe o tipo do produto'}),
            'marca':forms.TextInput(attrs={'placeholder':'Informe a marca do produto'}),
            'cor':forms.TextInput(attrs={'placeholder':'Informe a cor do produto'}),
            'qtd_disponivel':forms.TextInput(attrs={'placeholder':'Informe quantidade disponível do produto'}),
            'qtd_min_disponivel':forms.TextInput(attrs={'placeholder':'Informe quantidade mínima disponível do produto'}),
            'pco_custo':forms.TextInput(attrs={'placeholder':'Informe o preço de custo do produto'}),
            'pco_venda':forms.TextInput(attrs={'placeholder':'Informe o preço de venda do produto'}),
            'dt_ultima_compra':forms.TextInput(attrs={'placeholder':'Informe data da útima compra do produto'})
            
        }