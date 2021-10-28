from django import forms
from .models import VoluntarioParceiro

class FormNovoAgendamento(forms.Form): 
   nome = forms.CharField(required=True)
   email_origem = forms.EmailField(required=True, label = 'Entre com seu e-mail:')
   mensagem = forms.CharField(required=True)
   vol_par = VoluntarioParceiro