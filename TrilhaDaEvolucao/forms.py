from django import forms
from django.forms.models import ModelForm
from .models import VoluntarioParceiro, Familia, AreaPrograma, Agendamentos


class FormNovoAgendamentoVoluntario(forms.Form): 
   familia = forms.ModelChoiceField(queryset=Familia.objects.all().order_by('nome'))
   nome = forms.ModelChoiceField(queryset=VoluntarioParceiro.objects.all().order_by('nome'),label='Nome Voluntário / Parceiro')
   data = forms.DateTimeField(required=True,widget=forms.SelectDateWidget(),label='Data')
   hora = forms.CharField(required=True,widget=forms.TextInput(attrs={'type': 'time'}))
 
class FormNovoAgendamentoPrograma(forms.Form): 
   familia = forms.ModelChoiceField(queryset=Familia.objects.all().order_by('nome'))
   nome = forms.ModelChoiceField(queryset=AreaPrograma.objects.all().order_by('nome'),label='Área do Programa')
   data = forms.DateTimeField(required=True,widget=forms.SelectDateWidget(),label='Data')
   hora = forms.CharField(required=True,widget=forms.TextInput(attrs={'type': 'time'}))
 
class FormReAgendamentoVoluntario(forms.Form): 
   familia = forms.ModelChoiceField(queryset=Familia.objects.all().order_by('nome'))
   nome = forms.ModelChoiceField(queryset=VoluntarioParceiro.objects.all().order_by('nome'),label='Nome Voluntário / Parceiro')
   data = forms.DateTimeField(required=True,widget=forms.SelectDateWidget(),label='Data')
   hora = forms.CharField(required=True,widget=forms.TextInput(attrs={'type': 'time'}))
   idr = forms.IntegerField(required=False,widget=forms.HiddenInput())
 
class FormReAgendamentoPrograma(forms.Form): 
   familia = forms.ModelChoiceField(queryset=Familia.objects.all().order_by('nome'))
   nome = forms.ModelChoiceField(queryset=AreaPrograma.objects.all().order_by('nome'),label='Área do Programa')
   data = forms.DateTimeField(required=True,widget=forms.SelectDateWidget(),label='Data')
   hora = forms.CharField(required=True,widget=forms.TextInput(attrs={'type': 'time'}))
   idr = forms.IntegerField(required=False,widget=forms.HiddenInput())