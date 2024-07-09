from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


from dashboard.views import index
from cadastro_seller.views import (
    list_empresas,
    empresa_create,
    empresa_update,
    empresa_delete,
    detalhes_empresas,
    list_oportunidades,
    oportunidade_create,
    oportunidade_update,
    list_tarefas,
    tarefa_create,
    tarefa_update,
    kanban,
    update_status,
    list_leads,
    lead_create,
    kanban_oportunidade,
    update_kanban_op,
)
from usuarios.views import perfil, detalhes_perfil

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path("", index, name="index"),

    #URLS Empresas
    path('empresas/', list_empresas, name='list_empresas'),
    path("detalhes-seller/<int:pk>/", detalhes_empresas, name="detalhes_empresas"),

    # URLS do CRUD - Empresas
    path('empresas/new/', empresa_create, name='empresa_create'),
    path('empresas/<int:pk>/edit/', empresa_update, name='empresa_update'),
    path('empresas/<int:pk>/delete/', empresa_delete, name='empresa_delete'),

    #Perfil do Uduario:
    path('perfil/', detalhes_perfil, name='detalhes_perfil'),

    #URLS de Oportunidades
    path('oportunidades/', list_oportunidades, name='list_oportunidades'),
    path('oportunidades/new/', oportunidade_create, name='oportunidade_create'),
    path('oportunidades/<int:pk>/edit/', oportunidade_update, name='editar_oportunidade'),
    path('oportunidades-kanban/', kanban_oportunidade, name='kanban_oportunidade'),
    path('oportunidade-status-kanban/<int:id>/', update_kanban_op, name='update_kanban_op'),

    #URLS de Tarefas
    path('list-tarefas/', list_tarefas, name='list_tarefas'),
    path('tarefa/new', tarefa_create, name='tarefa_create'),
    path('tarefas/<int:pk>/edit/', tarefa_update, name='tarefa_update'),
    path('tarefas-kanban/', kanban, name='kanban'),
    path('tarefas-update-kanban/<int:id>/', update_status, name='update_kanban'),

    #URLS sobre Leads
    path('leads/', list_leads, name='list_leads'),
    path('leads/new/', lead_create, name='lead_create'),


    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)