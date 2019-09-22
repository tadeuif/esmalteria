from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model =  Agendamento
        fields = ['nome','dt_agendamento','hora_agendamento','servico_prestado']
        widgets = {
            'nome':forms.TextInput(attrs={'placeholder':'Nome cliente'}),
            'dt_agendamento':forms.TextInput(attrs={'placeholder':'Data de agendamento'}),
            'hora_agendamento':forms.TextInput(attrs={'placeholder':'Hora de agendamento'}),
            'servico_prestado':forms.TextInput(attrs={'placeholder':'Serviço prestado'})
          
            
        }