#admin.py
from django.contrib import admin

from .models import Familia, AreaPrograma, VoluntarioParceiro, AreaVoluntarioParceiro, AreaAtuacaoVoluntarioParceiro, AreaAcompanhamento

class FamiliaAdmin(admin.ModelAdmin):
    fields = ['nome', 'telefone', 'ano', 'nro_membros']
    list_display = ('id','nome', 'telefone', 'ano', 'nro_membros')

admin.site.register(Familia, FamiliaAdmin)

class AreaProgramaAdmin(admin.ModelAdmin):
    fields = ['nome', 'descricao']
    list_display = ('id','nome', 'descricao')

admin.site.register(AreaPrograma, AreaProgramaAdmin)

class VoluntarioParceiroAdmin(admin.ModelAdmin):
       fields = ['nome', 'telefone','disponibilidade']
       list_display = ('id','nome', 'telefone','disponibilidade')

admin.site.register(VoluntarioParceiro, VoluntarioParceiroAdmin)

class AreaVoluntarioParceiroAdmin(admin.ModelAdmin):
    fields = ['nome', 'descricao']
    list_display = ('id','nome', 'descricao')

admin.site.register(AreaVoluntarioParceiro, AreaVoluntarioParceiroAdmin)

class AreaAtuacaoVoluntarioParceiroAdmin(admin.ModelAdmin):
    fields = ['id_vol_par', 'id_area_vol_par']
    list_display = ('id','id_vol_par', 'id_area_vol_par')
    
admin.site.register(AreaAtuacaoVoluntarioParceiro, AreaAtuacaoVoluntarioParceiroAdmin)

class AreaAcompanhamentoAdmin(admin.ModelAdmin):
    fields = ['id_familia' ,    'id_area_programa' ,    'concluido' ,  'observacao',   'completude',     'data_termino'    ]
    list_display = ('id','id_familia' ,    'id_area_programa' ,    'concluido' ,   'observacao',   'completude', 'data_inicio',    'data_termino')

admin.site.register(AreaAcompanhamento, AreaAcompanhamentoAdmin )

    