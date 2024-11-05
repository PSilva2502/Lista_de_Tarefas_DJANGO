# tarefas/views.py
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Tarefa

# tarefas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'lista_tarefas.html', {'tarefas': tarefas})

def adicionar_tarefa(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        print(f"Título: {titulo}, Descrição: {descricao}")  # Log para verificação

        if titulo:  # Adiciona verificação para garantir que o título não está vazio
            Tarefa.objects.create(titulo=titulo, descricao=descricao)
        else:
            print("Título está vazio.")  # Log para verificar dados vazios

    return redirect('lista_tarefas')


def concluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.concluida = True
    tarefa.save()
    return redirect('lista_tarefas')

def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('lista_tarefas')

def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)

    if request.method == 'POST':
        novo_titulo = request.POST.get('titulo')
        if novo_titulo:
            tarefa.titulo = novo_titulo
            tarefa.save()
            return redirect('lista_tarefas')

    return render(request, 'editar_tarefa.html', {'tarefa': tarefa})