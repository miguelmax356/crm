from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json


from .models import Empresa, Oportunidade, Tarefa, Lead
from .forms import EmpresaForm, OportunidadeForm, TarefaForm, LeadForm
from usuarios.models import Usuario


# Nessa view adicionei filtro e ordenacao por titulo
@login_required
def list_empresas(request):
    query = request.GET.get('query')
    order_by = request.GET.get('order_by', 'titulo')
    direction = request.GET.get('direction','asc')

    if direction == 'asc':
        order_by_field = order_by
    else:
        order_by_field = f'-{order_by}'

    todas_empresas = Empresa.objects.all()

    if query:
        empresa = todas_empresas.filter(nome_icontains=query)

    context = {
        "todas_empresas": todas_empresas,
        'query': query,
        'order_by': order_by,
        'direction': direction,
    }

    return render (request, "empresa/lista_empresas.html", context)


@login_required
def detalhes_empresas(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    oportunidade = Oportunidade.objects.filter(empresa=empresa)
    tarefa = Tarefa.objects.filter(empresa=empresa)


    context = {
        "detalhes_empresa": empresa,
        "detalhes_oportunidade": oportunidade,
        "detalhes_tarefas": tarefa
    }
    return render(request, 'empresa/detalhes_seller.html', context)



# CRUD de empresa

def empresa_create(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_empresas')
    else:
        form = EmpresaForm()

    return render(request, 'empresa/criar_empresa.html', {'form': form})


def empresa_update(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    
    if request.method == 'POST':
        form_update = EmpresaForm(request.POST, instance=empresa)
        if form_update.is_valid():
            form_update.save()
            return HttpResponseRedirect(reverse('empresa_update', args=[pk]))
    else:
        form_update = EmpresaForm(instance=empresa)
    return render(request, 'empresa/editar_seller.html', {'form_update': form_update})


def empresa_delete(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        empresa.delete()
        return redirect(reverse('list_empresas'))
    return render(request, 'empresa/delete_empresa.html')


# Lista de Oportunidades

@login_required
def list_oportunidades(request):
    todas_oportunidades = Oportunidade.objects.all()
    
    return render (request, "oportunidade/lista_oportunidades.html", {"todas_oportunidades": todas_oportunidades})


@login_required
def kanban_oportunidade(request):
    usuario = request.user
    oportunidades = Oportunidade.objects.all()
    oportunidade_usuario = Oportunidade.objects.filter(usuario=usuario)

    return render(request, 'oportunidade/kanban_oportunidade.html', {
        'oportunidade_usuario': oportunidade_usuario,
        'usuario': usuario, 'oportunidades': oportunidades,
    })

@login_required
@csrf_exempt
@require_POST
def update_kanban_op(request, id):
    try:
        data = json.loads(request.body)
        status = data.get('status')
        oportunidade = Oportunidade.objects.get(id=id)
        oportunidade.status_negociacao = status
        oportunidade.save()
        return JsonResponse({'message': 'Status atualizado com sucesso!'}, status=200)
    except Oportunidade.DoesNotExist:
        return JsonResponse({'error': 'Oportunidade não encontrada.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


#Crud de oportunidade
@login_required
def oportunidade_create(request):
    if request.method == 'POST':
        form = OportunidadeForm(request.POST)
        if form.is_valid():
            oportunidade = form.save(commit=False)
            oportunidade.usuario = request.user  # Define o usuário atual como o criador da oportunidade
            oportunidade.save()
            return redirect('list_oportunidades')
    else:
        form = OportunidadeForm()
    
    return render(request, 'oportunidade/criar_oportunidade.html', {'form': form})




def oportunidade_update(request, pk):
    oportunidade = get_object_or_404(Oportunidade, pk=pk)

    if request.method == 'POST':
        form_oportunidade = OportunidadeForm(request.POST, instance=oportunidade)
        if form_oportunidade.is_valid():
            form_oportunidade.save()
            return HttpResponseRedirect(reverse('editar_oportunidade', args=[pk]))
    else:
        form_oportunidade = OportunidadeForm(instance=oportunidade)

    return render(request, 'oportunidade/editar_oportunidade.html', {
        'form_oportunidade': form_oportunidade,
        'status': oportunidade.status_negociacao  # Passa o status da oportunidade para o template
    })



# Viwes de Tarefas

def list_tarefas(request):
    list_tarefas = Tarefa.objects.all()

    return render(request, 'tarefas/list_tarefas.html', {'list_tarefas': list_tarefas})



@login_required
def tarefa_create(request):
    if request.method == 'POST':
        form_tarefa = TarefaForm(request.POST)
        if form_tarefa.is_valid():
            tarefa = form_tarefa.save(commit=False)
            tarefa.usuario = request.user
            
            # Verifica se o campo empresa está preenchido no formulário
            if 'empresa' in request.POST and request.POST['empresa']:
                tarefa.empresa_id = request.POST['empresa']
            
            tarefa.save()
            return redirect('list_tarefas')
    else:
        form_tarefa = TarefaForm()

    return render(request, 'tarefas/criar_tarefa.html', {'form_tarefa': form_tarefa})




@login_required
def tarefa_update(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    if request.method == 'POST':
        form_tarefa = TarefaForm(request.POST, instance=tarefa)
        if form_tarefa.is_valid():
            form_tarefa.save()
            return redirect('list_tarefas')  # Certifique-se de que 'list_tarefas' é uma URL nomeada válida
    else:
        form_tarefa = TarefaForm(instance=tarefa)

    return render(request, 'tarefas/editar_tarefa.html', {'form_tarefa': form_tarefa})


# Viewa para o Kanban de Tarefas

@login_required
def kanban(request):
    tarefas = Tarefa.objects.all()
    usuario = request.user  # Obtém o usuário atualmente logado
    tarefas_usuario = Tarefa.objects.filter(usuario=usuario)

    return render(request, 'tarefas/kanban.html', {'tarefas': tarefas, 'usuario': usuario, 'tarefas_usuario': tarefas_usuario})



@login_required
@csrf_exempt
@require_POST
def update_status(request, id):
    try:
        data = json.loads(request.body)
        status = data.get('status')
        tarefa = Tarefa.objects.get(id=id)
        tarefa.status = status
        tarefa.save()
        return JsonResponse({'message': 'Status atualizado com sucesso!'}, status=200)
    except Tarefa.DoesNotExist:
        return JsonResponse({'error': 'Tarefa não encontrada.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)



# Views sobre LEads 
@login_required
def list_leads(request):

    list_leads = Lead.objects.all()
    return render(request, 'leads/lista_leads.html', {'list_leads': list_leads})



@login_required
def lead_create(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_leads')
    else:
        form = LeadForm()
    return render(request, 'leads/criar_lead.html', {'form': form})




