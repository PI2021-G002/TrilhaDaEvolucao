from django.utils.formats import date_format
from django.views.generic.base import View
from django.views.generic.edit import FormView
from .models import Agendamentos, AreaPrograma, Familia, VoluntarioParceiro
from TrilhaDaEvolucao import forms
from django.shortcuts import render
from datetime import date 
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import FormNovoAgendamentoVoluntario
from datetime import date, datetime
from django.db import connection
import MySQLdb

def NovoAgendamentoVolParc(request):
   # if this is a POST request we need to process the form data
   if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = FormNovoAgendamentoVoluntario(request.POST)
      # check whether it's valid:
        
      if form.is_valid():
           
        # if (form.cleaned_data['data'].isoformat() >= datetime.now().isoformat()):
              ### save data
            data = request.POST.__getitem__('data_year') + '-' + request.POST.__getitem__('data_month') + '-' + request.POST.__getitem__('data_day')
            hora = request.POST.__getitem__('hora')
            familia = Familia()
            familia.id=request.POST.__getitem__('familia')
            tipo = 'V'
            id_tipo = request.POST.__getitem__('nome')
            #return HttpResponse(data_hora)
            agendamento = Agendamentos.objects.create(data=data,time=hora,id_familia=familia,tipo=tipo,id_tipo=id_tipo)
            return HttpResponse("Agendamento Criado com Sucesso")
               
         #else:
               
         #       return render(request, 'NovoAgendamento.html', {'form': form})



    # if a GET (or any other method) we'll create a blank form
   else:
      form = FormNovoAgendamentoVoluntario()

      return render(request, 'NovoAgendamento.html', {'form': form}) 

 

def NovoAgendamentoPrograma(request):
   # if this is a POST request we need to process the form data
   if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = FormNovoAgendamentoVoluntario(request.POST)
      # check whether it's valid:
        
      if form.is_valid():
           
        # if (form.cleaned_data['data'].isoformat() >= datetime.now().isoformat()):
              ### save data
            data = request.POST.__getitem__('data_year') + '-' + request.POST.__getitem__('data_month') + '-' + request.POST.__getitem__('data_day')
            hora = request.POST.__getitem__('hora')
            familia = Familia()
            familia.id=request.POST.__getitem__('familia')
            tipo = 'P'
            id_tipo = request.POST.__getitem__('nome')
            #return HttpResponse(data_hora)
            agendamento = Agendamentos.objects.create(data=data,time=hora,id_familia=familia,tipo=tipo,id_tipo=id_tipo)
            return HttpResponse("Agendamento Criado com Sucesso")
               
         #else:
               
         #       return render(request, 'NovoAgendamento.html', {'form': form})



    # if a GET (or any other method) we'll create a blank form
   else:
      form = FormNovoAgendamentoVoluntario()

      return render(request, 'NovoAgendamento.html', {'form': form}) 

@login_required
def ViewAgendamentos(request):
   hoje = date.today()
   semana = hoje.isocalendar()[1]  # retorna a semana do ano para a data
   mes = hoje.month
   return render(request,'Agendamentos.html',
   {
       'hoje'    : hoje.isoformat(),
       'v_dia'   : Agendamentos.objects.filter(data__day = hoje.day)
                                       .filter(data__month = hoje.month)
                                       .filter(data__year = hoje.year).order_by('data').order_by('time'),
       'semana'  : semana,
       'v_semana': Agendamentos.objects.filter(data__week = semana).order_by('data').order_by('time'),
       'mes'     : mes,
       'v_mes'   : Agendamentos.objects.filter(data__month = mes).order_by('data').order_by('time'),

   } )

def logout_view(request):
    logout(request)
    return render(request,'index.html')

def fromCursorToTableData(cursor,rows):
   x = cursor.description
   resultsList = []   
   for r in rows:
      i = 0
      d = {}
      while i < len(x):
         d[x[i][0]] = r[i]
         i = i+1
      resultsList.append(d)
   return resultsList

def getAcompanhentoCount():
    with connection.cursor() as cursor:
        cursor.execute('select ap.nome, count(*) as numero, sum(aa.completude) / count(*) as media from TrilhaDaEvolucao_areaacompanhamento aa, TrilhaDaEvolucao_areaprograma ap where aa.id_area_programa_id = ap.id group by id_area_programa_id order by ap.nome')
        row = cursor.fetchall()
        result = fromCursorToTableData(cursor,row)
    return result

def getAcompanhentos():
    with connection.cursor() as cursor:
        cursor.execute('select f.nome as familia, ap.nome as area, aa.completude from TrilhaDaEvolucao_areaacompanhamento aa, TrilhaDaEvolucao_familia f, TrilhaDaEvolucao_areaprograma ap WHERE aa.id_area_programa_id = ap.id AND   aa.id_familia_id = f.id order by f.nome,ap.nome')
        row = cursor.fetchall()
        result = fromCursorToTableData(cursor,row)
    return result

@login_required
def ViewAcompanhamentos(request):
   acomp_count = getAcompanhentoCount()
   acomp_familias = getAcompanhentos()
   return render(request,'Acompanhamento.html',
   {
       'acomp_histogram'    : acomp_count,
       'dados_familias' : acomp_familias,
       'familias_count' : Familia.objects.count(),
       'areas_count'    : AreaPrograma.objects.count(),

 
   } )

   

