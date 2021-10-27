from django.views.generic.edit import FormView
from TrilhaDaEvolucao import forms

class NovoAgendamento(FormView):
   template_name = "NovoAgendamento.html"
   form_class = forms.FormNovoAgendamento
   success_url = "/"