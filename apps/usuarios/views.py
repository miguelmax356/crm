from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from usuarios.models import Usuario


@login_required
def perfil(request):

    return render(request, "base.html")




@login_required
def detalhes_perfil(request):


    return render(request, "perfil_usuario/perfil.html")