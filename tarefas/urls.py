from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),  # Define '' para acessar diretamente a lista de tarefas
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('concluir/<int:id>/', views.concluir_tarefa, name='concluir_tarefa'),
    path('excluir/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
]
