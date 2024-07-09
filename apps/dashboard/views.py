from django.shortcuts import render
from cadastro_seller.models import Empresa, Oportunidade, Lead



def index(request):
    
    empresas = Empresa.objects.all()
    oportunidades = Oportunidade.objects.all()
    leads = Lead.objects.all()

    empresas = empresas.exclude(empresa='')
    oportunidades_negociacao = oportunidades.filter(status_negociacao='em negociação')
    oportunidades_ganhas = oportunidades.filter(status_negociacao='ganha')
    oportunidades_totais = oportunidades.exclude(status_negociacao='')
    leads = leads.exclude(nome_empresa='')


    context = {
        'empresas': empresas.count(),
        'oportunidades_negociacao': oportunidades_negociacao.count(),
        'oportunidades_ganhas': oportunidades_ganhas.count(),
        'oportunidades_totais': oportunidades_totais.count(),
        'leads': leads.count()
    }

    return render(request, "dashboard.html", context)
