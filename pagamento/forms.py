from django import forms
from .models import Pagamento


#status_choices = ['Aberto','Pendente','Concluido']

class PagamentoForm(forms.ModelForm):
    class Meta:
        model =  Pagamento
        fields = ['nome','cod_servico','cod_cliente','valor_pagamento','dt_pagamento','status']
        #choice_fields = forms.ChoiceField(widget=forms.Select,choices=status_choices)
        widgets = {
            'nome':forms.TextInput(attrs={'placeholder':'Informe o nome'}),
            'cod_servico':forms.TextInput(attrs={'placeholder':'Informe o codigo do servico'}),
            'cod_cliente':forms.TextInput(attrs={'placeholder':'Informe o codigo do cliente'}),
            'valor_pagamento':forms.TextInput(attrs={'placeholder':'Informe o valor do pagamento a ser recebido'}),
            'dt_pagamento':forms.TextInput(attrs={'placeholder':'Informe a data do pagamento'})            
        }