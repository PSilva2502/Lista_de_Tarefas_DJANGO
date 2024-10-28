<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
</head>
<body>

<h1>📋 Minha Lista de Tarefas</h1>

![image](https://github.com/user-attachments/assets/5a85019c-05ac-42e3-a7eb-8e255f4db255) <br>
![image](https://github.com/user-attachments/assets/89ea1dd5-7f40-47e4-b6f4-b20f41af6718)



<p>Este é um projeto simples de lista de tarefas, onde o usuário pode adicionar, visualizar e gerenciar suas tarefas diárias.</p>

<h2>🎯 Funcionalidades</h2>
<ul>
    <li>Adicionar uma nova tarefa com um título e uma descrição.</li>
    <li>Visualizar uma lista de tarefas adicionadas.</li>
    <li>Organizar e gerenciar as tarefas de forma intuitiva.</li>
</ul>

<h2>🚀 Como Usar</h2>

<p>Este passo a passo mostra como configurar o ambiente e executar o sistema localmente:</p>

<ol>
  <li>
    <strong>Pré-requisitos:</strong>
    <ul>
      <li>Certifique-se de ter o <strong>Python</strong> instalado em sua máquina. Você pode baixá-lo no <a href="https://www.python.org/downloads/">site oficial do Python</a>.</li>
      <li>Opcional: Recomenda-se instalar o <strong>Git</strong> para clonar o repositório (se ainda não tiver baixado o código).</li>
    </ul>
  </li>
  
  <li>
    <strong>Clone o repositório:</strong>
    <ol>
      <li>Abra o terminal e execute o comando abaixo para clonar o repositório do GitHub (substitua <code>&lt;url-do-repositorio&gt;</code> pela URL do seu repositório):
        <pre><code>git clone &lt;url-do-repositorio&gt;</code></pre>
      </li>
      <li>Acesse a pasta do projeto:
        <pre><code>cd nome-da-pasta-do-projeto</code></pre>
      </li>
    </ol>
  </li>
  
  <li>
    <strong>Crie e ative um ambiente virtual:</strong>
    <ol>
      <li>No terminal, execute:
        <pre><code>python -m venv venv</code></pre>
      </li>
      <li>Ative o ambiente virtual:
        <ul>
          <li>No <strong>Windows</strong>:
            <pre><code>venv\Scripts\activate</code></pre>
          </li>
          <li>No <strong>macOS/Linux</strong>:
            <pre><code>source venv/bin/activate</code></pre>
          </li>
        </ul>
      </li>
    </ol>
  </li>
  
  <li>
    <strong>Instale as dependência:</strong>
    <ul>
      <li>Com o ambiente virtual ativado, instale as dependências do projeto (supondo que elas estejam listadas em um arquivo <code>requirements.txt</code>):
        <pre><code>pip install -r requirements.txt</code></pre>
      </li>
    </ul>
  </li>

  <li>
    <strong>Instale o DJANGO:</strong>
    <ul>
      <li>Com o ambiente virtual ativado, instale o DJANGO <code>DJANGO</code>):
        <pre><code>pip install DJANGO</code></pre>
      </li>
    </ul>
  </li>
  
  <li>
    <strong>Configuração do Banco de Dados:</strong>
    <ul>
      <li>Execute as migrações para configurar o banco de dados:
        <pre><code>python manage.py migrate</code></pre>
      </li>
    </ul>
  </li>
  
  <li>
    <strong>Execute o servidor:</strong>
    <ul>
      <li>Inicie o servidor Django:
        <pre><code>python manage.py runserver</code></pre>
      </li>
    </ul>
  </li>
  
  <li>
    <strong>Utilize o Sistema:</strong>
    <ul>
      <li>Agora você pode adicionar, visualizar e gerenciar suas tarefas pelo sistema de lista de tarefas.</li>
    </ul>
  </li>
  
  <li>
    <strong>Desativando o Ambiente Virtual:</strong>
    <ul>
      <li>Após terminar de usar o sistema, desative o ambiente virtual executando:
        <pre><code>deactivate</code></pre>
      </li>
    </ul>
  </li>
</ol>


<h2>🛠️ Tecnologias Utilizadas</h2>
<ul>
    <li>HTML5</li>
    <li>CSS3</li>
    <li>JavaScript</li>
    <li>Python</li>
</ul>

<h2>📄 Licença</h2>
<p>Este projeto está licenciado sob a Licença MIT. Veja o texto completo da licença abaixo:</p>

<pre>
MIT License

Copyright (c) [2024] [Pedro Silva]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</pre>

</body>
</html>
