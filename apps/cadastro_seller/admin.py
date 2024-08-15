from django.contrib import admin
from cadastro_seller.models import Empresa, Oportunidade, Tarefa, Lead
from .forms import TarefaForm

from contatos.admin import ContatoInline



class TarefaInline(admin.TabularInline):
    model = Tarefa
    extra = 0
    fields = ('atividade','negocio', 'empresa', 'telefone', 'email', 'descricao', 'status','usuario')


class TarefaAdmin(admin.ModelAdmin):
    list_display = ('contato', 'atividade', 'telefone', 'email', 'status', 'negocio', 'usuario')


class OportunidadeAdmin(admin.ModelAdmin):
    form = TarefaForm
    list_display = ('empresa', 'titulo', 'status_negociacao', 'usuario', 'probabilidade', 'taxa_comissao', 'data_fechamento')
    inlines = [TarefaInline, ContatoInline]


class OportunidadeInline(admin.TabularInline):
    model = Oportunidade
    extra = 0
    fields = ('titulo', 'status_negociacao', 'usuario', 'probabilidade', 'taxa_comissao', 'data_fechamento', 'arquivo')


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'telefone', 'email', 'segmento')
    search_fields = ('empresa', 'email')
    list_filter = ('empresa', 'telefone')
    inlines = [OportunidadeInline, TarefaInline, ContatoInline]


@admin.action(description='Converter Lead para Empresa')
def converter_para_empresa(modeladmin, request, queryset):
    for lead in queryset:
        empresa = lead.converter_para_empresa()
        empresa.save()
        lead.delete()


class LeadAdmin(admin.ModelAdmin):
    list_display = ('nome_empresa', 'contato_lead', 'email_lead')
    search_fields = ('nome_empresa', 'email_lead')
    list_filter = ('nome_empresa', 'telefone_lead')
    actions = [converter_para_empresa]



admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Oportunidade, OportunidadeAdmin)
admin.site.register(Tarefa, TarefaAdmin)
admin.site.register(Lead, LeadAdmin)
