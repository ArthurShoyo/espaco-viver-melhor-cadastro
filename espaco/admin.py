from django.contrib import admin

from .models import Atendimentos, Pessoa

# Register your models here.

class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'tecnicaaplicada', 'dataatend')
    list_display_links = ('id', 'nome',)
    list_filter = ('nome', 'tecnicaaplicada')
    list_per_page = 10
    search_fields = ('nome',)

admin.site.register(Pessoa)
admin.site.register(Atendimentos, AtendimentoAdmin)
