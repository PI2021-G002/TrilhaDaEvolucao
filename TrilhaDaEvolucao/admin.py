#admin.py
from django.contrib import admin

from .models import Familia, AreaPrograma, Voluntario, Parceiro, AreaVoluntario, AreaParceiro, AreaAtuacaoVoluntario, AreaAtuacaoParceiro, AreaAcompanhamento

class FamiliaAdmin(admin.ModelAdmin):
    fields = ['nome', 'telefone', 'ano', 'nro_membros']
    list_display = ('id','nome', 'telefone', 'ano', 'nro_membros')

admin.site.register(Familia, FamiliaAdmin)

class AreaProgramaAdmin(admin.ModelAdmin):
    fields = ['nome', 'descricao']
    list_display = ('id','nome', 'descricao')

admin.site.register(AreaPrograma, AreaProgramaAdmin)

class VoluntarioAdmin(admin.ModelAdmin):
       fields = ['nome', 'telefone','disponibilidade']
       list_display = ('id','nome', 'telefone','disponibilidade')

admin.site.register(Voluntario, VoluntarioAdmin)

class ParceiroAdmin(admin.ModelAdmin):
       fields = ['nome', 'telefone','disponibilidade']
       list_display = ('id','nome', 'telefone','disponibilidade')

admin.site.register(Parceiro, ParceiroAdmin)

class AreaVoluntarioAdmin(admin.ModelAdmin):
    fields = ['nome', 'descricao']
    list_display = ('id','nome', 'descricao')

admin.site.register(AreaVoluntario, AreaVoluntarioAdmin)

class AreaParceiroAdmin(admin.ModelAdmin):
    fields = ['nome', 'descricao']
    list_display = ('id','nome', 'descricao')

admin.site.register(AreaParceiro, AreaParceiroAdmin)

class AreaAtuacaoVoluntarioAdmin(admin.ModelAdmin):
    fields = ['id_vol', 'id_area_vol', 'descricao']
    list_display = ('id','id_vol', 'id_area_vol', 'descricao')
    
admin.site.register(AreaAtuacaoVoluntario, AreaAtuacaoVoluntarioAdmin)

class AreaAtuacaoParceiroAdmin(admin.ModelAdmin):
    fields = ['id_par', 'id_area_par', 'descricao']
    list_display = ('id','id_par', 'id_area_par', 'descricao')
    
admin.site.register(AreaAtuacaoParceiro, AreaAtuacaoParceiroAdmin)

class AreaAcompanhamentoAdmin(admin.ModelAdmin):
    fields = ['id_familia' ,    'id_area_programa' ,    'concluido' ,  'observacao',   'completude',     'data_termino'    ]
    list_display = ('id','id_familia' ,    'id_area_programa' ,    'concluido' ,   'observacao',   'completude', 'data_inicio',    'data_termino')

admin.site.register(AreaAcompanhamento, AreaAcompanhamentoAdmin )

    