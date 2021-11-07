from django.utils.formats import date_format
from .models import Agendamentos, AreaPrograma, Familia
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import FormNovoAgendamentoPrograma, FormNovoAgendamentoVoluntario, FormReAgendamentoVoluntario, FormReAgendamentoPrograma
from datetime import date, datetime
from django.db import connection
from django.contrib import messages

def NovoAgendamentoVolParc(request,id=0):
   # if this is a POST request we need to process the form data
   if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = FormNovoAgendamentoVoluntario(request.POST)
      # check whether it's valid:
        
      if form.is_valid() and (form.cleaned_data['data'].isoformat() >= datetime.now().isoformat()):
         ### save data
         data = request.POST.__getitem__('data_year') + '-' + request.POST.__getitem__('data_month') + '-' + request.POST.__getitem__('data_day')
         hora = request.POST.__getitem__('hora')
         familia = Familia()
         familia.id=request.POST.__getitem__('familia')
         tipo = 'V'
         id_tipo = request.POST.__getitem__('nome')
         agendamento = Agendamentos.objects.create(data=data,hora=hora,id_familia=familia,tipo=tipo,id_tipo=id_tipo)
         messages.success(request,"Agendamento Criado com Sucesso")
    # if a GET (or any other method) we'll create a blank or filled form
   else:
         form = FormNovoAgendamentoVoluntario()
   return render(request, 'NovoAgendamento.html', {'form': form})

def ReAgendamentoVolParc(request,id=0):
   # if this is a POST request we need to process the form data
   if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = FormReAgendamentoVoluntario(request.POST)
      # check whether it's valid:
       
      if form.is_valid() and (form.cleaned_data['data'].isoformat() >= datetime.now().isoformat()):
         ### save data
         data = request.POST.__getitem__('data_year') + '-' + request.POST.__getitem__('data_month') + '-' + request.POST.__getitem__('data_day')
         hora = request.POST.__getitem__('hora')
         familia = Familia()
         familia.id=request.POST.__getitem__('familia')
         tipo = 'V'
         id_tipo = request.POST.__getitem__('nome')
         agendamento = Agendamentos.objects.create(data=data,hora=hora,id_familia=familia,tipo=tipo,id_tipo=id_tipo)
         if request.POST.__getitem__('idr'):
            agendamento = Agendamentos.objects.filter(id=request.POST.__getitem__('idr'))
            agendamento.delete()
         messages.success(request,"Agendamento Criado com Sucesso")
    # if a GET (or any other method) we'll create a blank or filled form
   else:
      evento = Agendamentos.objects.filter(id=id)
      #return HttpResponse(evento)
      #dados = {'id': id, 'tipo': evento.tipo, 'data': evento.data, 'hora': evento.hora, 'id_tipo': evento.id_tipo, 'id_familia': evento.id_familia_id}
      # {'id': 3, 'data': datetime.date(2021, 11, 28), 'hora': None, 'id_familia_id': 1, 'tipo': 'A', 'id_tipo': 1}
      form = FormReAgendamentoVoluntario(initial={
         'data' : evento[0].data, 
         'hora' : evento[0].hora,
         'nome': evento[0].id_tipo,
         'familia': evento[0].id_familia_id,
         'tipo': evento[0].tipo,
         'idr': id
         })
   return render(request, 'NovoAgendamento.html', {'form': form})

def NovoAgendamentoPrograma(request,id=0):
   # if this is a POST request we need to process the form data
   if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = FormNovoAgendamentoPrograma(request.POST)
      # check whether it's valid:
        
      if form.is_valid():
         ### save data
         data = request.POST.__getitem__('data_year') + '-' + request.POST.__getitem__('data_month') + '-' + request.POST.__getitem__('data_day')
         hora = request.POST.__getitem__('hora')
         familia = Familia()
         familia.id=request.POST.__getitem__('familia')
         tipo = 'P'
         id_tipo = request.POST.__getitem__('nome')
         agendamento = Agendamentos.objects.create(data=data,hora=hora,id_familia=familia,tipo=tipo,id_tipo=id_tipo)
         messages.success(request,"Agendamento Criado com Sucesso")

    # if a GET (or any other method) we'll create a blank form
   else:
         form = FormNovoAgendamentoPrograma()
   return render(request, 'NovoAgendamento.html', {'form': form})

def ReAgendamentoPrograma(request,id=0):
   # if this is a POST request we need to process the form data
   if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = FormReAgendamentoPrograma(request.POST)
      # check whether it's valid:
      if form.is_valid():
         ### save data
         data = request.POST.__getitem__('data_year') + '-' + request.POST.__getitem__('data_month') + '-' + request.POST.__getitem__('data_day')
         hora = request.POST.__getitem__('hora')
         familia = Familia()
         familia.id=request.POST.__getitem__('familia')
         tipo = 'P'
         id_tipo = request.POST.__getitem__('nome')
         
         agendamento = Agendamentos.objects.create(data=data,hora=hora,id_familia=familia,tipo=tipo,id_tipo=id_tipo)

         if request.POST.__getitem__('idr'):
            agendamento = Agendamentos.objects.filter(id=request.POST.__getitem__('idr'))
            agendamento.delete()
         messages.success(request,"Agendamento Criado com Sucesso")

    # if a GET (or any other method) we'll create a blank form
   else:
      evento = Agendamentos.objects.filter(id=id)
      #return HttpResponse(evento)
      #dados = {'id': id, 'tipo': evento.tipo, 'data': evento.data, 'hora': evento.hora, 'id_tipo': evento.id_tipo, 'id_familia': evento.id_familia_id}
      # {'id': 3, 'data': datetime.date(2021, 11, 28), 'hora': None, 'id_familia_id': 1, 'tipo': 'A', 'id_tipo': 1}
      form = FormReAgendamentoPrograma(initial={
         'data' : evento[0].data, 
         'hora' : evento[0].hora,
         'nome': evento[0].id_tipo,
         'familia':evento[0].id_familia_id,
         'tipo': evento[0].tipo,
         'idr': id
         })
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
                                       .filter(data__year = hoje.year).order_by('data').order_by('hora'),
       'semana'  : semana,
       'v_semana': Agendamentos.objects.filter(data__week = semana).order_by('data').order_by('hora'),
       'mes'     : mes,
       'v_mes'   : Agendamentos.objects.filter(data__month = mes).order_by('data').order_by('hora'),

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
