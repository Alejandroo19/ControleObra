from django.contrib import admin
from .models import Obra, ValorAdicionado

class ObraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'valor', 'status')  # Colunas exibidas no admin
    search_fields = ('nome', 'status')  # Campos de pesquisa
    list_filter = ('status',)  # Filtros laterais
    ordering = ('nome',)  # Ordenação padrão

class ValorAdicionadoAdmin(admin.ModelAdmin):
    list_display = ('obra', 'valor', 'descricao', 'data')
    search_fields = ('obra__nome', 'descricao')  # Pesquisa no nome da obra e descrição
    list_filter = ('data',)  # Filtro por data

admin.site.register(Obra, ObraAdmin)
admin.site.register(ValorAdicionado, ValorAdicionadoAdmin)
