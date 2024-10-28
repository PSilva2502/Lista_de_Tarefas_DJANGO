Lista de Tarefas
Este é um projeto simples de Lista de Tarefas criado com Django. O projeto permite que os usuários adicionem tarefas com uma descrição, exibindo-as em uma interface amigável. Ao clicar em uma tarefa, a descrição completa é exibida em um modal.

![image](https://github.com/user-attachments/assets/ce92a12f-b082-4dcf-bfcb-a167e3d7e232)

![image](https://github.com/user-attachments/assets/798ed845-a27e-4165-9653-bcf4f36c25a7)


Página Inicia

Funcionalidades
Adicionar uma nova tarefa com um título e uma descrição.
Exibir as tarefas em uma lista.
Clicar em uma tarefa para visualizar a descrição completa em um modal.
<br>
Tecnologias Utilizadas:
<br>
Python
Django
HTML/CSS
JavaScript
<br>
Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas:
<br>
  Python 3.x
  Git

Instalação
1 - Clone o repositório:<br>
  git clone https://github.com/seu_usuario/nome_do_repositorio.git

2 - Navegue para o diretório do projeto:<br>
  cd nome_do_repositorio

3 - Crie um ambiente virtual:<br>
  python -m venv venv

4 - Ative o ambiente virtual:<br>
  Windows:<br>
  venv\Scripts\activate
  <br>
  No Linux/Mac:<br>
  source venv/bin/activate

5 - Instale o Django:<br>
  pip install django

6 - Execute as migrações do banco de dados:<br>
  python manage.py migrate

7 - Inicie o servidor de desenvolvimento:<br>
  python manage.py runserver

Estrutura do Projeto<br>
templates/: Contém os arquivos HTML.
static/: Contém os arquivos CSS e JavaScript.
tarefas/: Diretório principal da aplicação Django.

Como Usar<br>
1 - Na página inicial, insira o título e a descrição da tarefa nos campos correspondentes.<br>
2 - Clique em "Adicionar Tarefa" para adicionar a tarefa à lista.<br>
3 - Clique em qualquer tarefa na lista para visualizar sua descrição completa em um modal.
<br>
Licença<br>
Este projeto está sob a licença MIT.
