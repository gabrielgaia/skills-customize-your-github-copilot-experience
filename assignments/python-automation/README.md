# 📘 Atividade: Python Automation Basics

## 🎯 Objetivo

Praticar conceitos fundamentais de Python para criar scripts úteis que automatizam tarefas repetitivas, como organizar arquivos e resumir informações de forma simples e eficiente.

## 📝 Tarefas

### 🛠️ Organizar Arquivos por Extensão

#### Descrição
Crie um script em Python que leia uma pasta e mova os arquivos para subpastas de acordo com a extensão do arquivo.

#### Requisitos
O programa concluído deve:

- Receber como entrada o caminho de uma pasta.
- Verificar se a pasta existe antes de processar os arquivos.
- Criar uma subpasta para cada extensão encontrada, como `txt`, `py`, `csv` e `jpg`.
- Mover cada arquivo para a pasta correta, mantendo o nome original do arquivo.
- Ignorar pastas e arquivos que já estejam organizados.
- Exibir ao final um resumo com o número de arquivos movidos e as pastas criadas.

Exemplo de saída:

```python
Organizing files in: /home/aluno/downloads
Created folder: /home/aluno/downloads/txt
Created folder: /home/aluno/downloads/py
Moved 3 files
```

### 🛠️ Criar um Resumo de Tarefas

#### Descrição
Crie uma função que receba uma lista de tarefas e retorne um resumo simples com quantas tarefas estão concluídas, pendentes e em andamento.

#### Requisitos
O programa concluído deve:

- Usar listas e dicionários para representar tarefas.
- Permitir que cada tarefa tenha pelo menos três campos: `titulo`, `status` e `descricao`.
- Contar quantas tarefas estão em cada status: `concluida`, `pendente` e `em_andamento`.
- Mostrar um resumo final em formato legível para o usuário.
- Tratar casos em que a lista de tarefas esteja vazia com uma mensagem adequada.

Exemplo de uso:

```python
tasks = [
    {"titulo": "Estudar Python", "status": "concluida", "descricao": "Revisar listas e condicionais"},
    {"titulo": "Fazer exercícios", "status": "pendente", "descricao": "Resolver 5 problemas"},
    {"titulo": "Preparar projeto", "status": "em_andamento", "descricao": "Organizar arquivos e código"}
]

print(task_summary(tasks))
# Resumo: 1 concluída, 1 pendente, 1 em andamento
```
