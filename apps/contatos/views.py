from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponseRedirect, HttpResponse
from django.urls import reverse



from contatos.models import Contato
from .forms import ContatoForm




@login_required
def contatos(request):
    contatos = Contato.objects.all()

    return render(request, 'contatos/lista_contatos.html', {'contatos': contatos})


@login_required
def create_contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_contatos')
    else:
        form = ContatoForm()

    return render(request, 'contatos/criar_contato.html', {'form': form})


@login_required
def contato_update(request, pk):
    contato = get_object_or_404(Contato, pk=pk)

    if request.method == 'POST':
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contato_update', args=[pk]))
    else:
        form = ContatoForm(instance=contato)
    return render(request, 'contatos/editar_contatos.html', {'form': form})



            