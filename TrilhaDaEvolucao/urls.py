"""TrilhaDaEvolucao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from TrilhaDaEvolucao import views

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'), name='index'),
    path('accounts/logout',views.logout_view, name='Logout'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ajuda/',TemplateView.as_view(template_name='ajuda.html'), name='Ajuda'),
    path('agendamentos/',views.ViewAgendamentos, name='agendamento'),  
    path('agendamentos/novo/programa',views.NovoAgendamento.as_view(),name = 'NovoAgendamento'),
    path('agendamentos/novo/volparc',views.NovoAgendamento.as_view(),name = 'NovoAgendamento'),

]
