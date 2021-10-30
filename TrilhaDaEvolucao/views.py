from django.views.generic.base import View
from django.views.generic.edit import FormView
from .models import Agendamentos
from TrilhaDaEvolucao import forms
from django.shortcuts import render
from datetime import date 
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout

class NovoAgendamento(FormView):
   template_name = "NovoAgendamento.html"
   form_class = forms.FormNovoAgendamentoVoluntario
   success_url = "/"

@login_required
def ViewAgendamentos(request):
   hoje = date.today()
   semana = hoje.isocalendar()[1]  # retorna a semana do ano para a data
   mes = hoje.month
   return render(request,'Agendamentos.html',
   {
       'hoje'    : hoje.isoformat(),
       'v_dia'   : Agendamentos.objects.filter(data_hora__day = hoje.day)
                                       .filter(data_hora__month = hoje.month)
                                       .filter(data_hora__year = hoje.year),
       'semana'  : semana,
       'v_semana': Agendamentos.objects.filter(data_hora__week = semana),
       'mes'     : mes,
       'v_mes'   : Agendamentos.objects.filter(data_hora__month = mes),

   } )


def logout_view(request):
    logout(request)
    return render(request,'index.html')