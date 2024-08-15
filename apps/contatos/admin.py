from django.contrib import admin
from contatos.models import Contato


class ContatoAdmin(admin.ModelAdmin):
    
    list_display = ('nome', 'telefone', 'email', 'negocio')
    search_fields = ('nome', 'telefone', 'email', 'negocio')



class ContatoInline(admin.TabularInline):
    model = Contato
    extra = 0
    fields = ('nome', 'negocio', 'email', 'telefone')




admin.site.register(Contato, ContatoAdmin)