# tarefas/views.py
from django.shortcuts import render, redirect
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})

def adicionar_tarefa(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        Tarefa.objects.create(titulo=titulo, descricao=descricao)
    return redirect('lista_tarefas')  # Redireciona para a página de lista de tarefas
