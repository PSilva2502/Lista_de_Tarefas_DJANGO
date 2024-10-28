from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.lista_tarefas, name='lista_tarefas'),
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
]
