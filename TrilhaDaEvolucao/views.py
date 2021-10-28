from django.views.generic.base import View
from django.views.generic.edit import FormView
from .models import Agendamentos
from TrilhaDaEvolucao import forms
from django.shortcuts import render

class NovoAgendamento(FormView):
   template_name = "NovoAgendamento.html"
   form_class = forms.FormNovoAgendamento
   success_url = "/"

def ViewAgendamentos(request):
   return render(request,'Agendamentos.html',{'dia': Agendamentos.object.all()})
