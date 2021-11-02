from django import forms
from .models import VoluntarioParceiro, Familia, AreaPrograma


class FormNovoAgendamentoVoluntario(forms.Form): 
   nome = forms.CharField(required=True)
   
   data = forms.DateTimeField(required=True)
   familia = Familia.objects.all()
   vol_par = VoluntarioParceiro.objects.all()