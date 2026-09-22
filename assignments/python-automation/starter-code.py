from pathlib import Path


def organize_files(folder_path):
    """
    Organiza arquivos de uma pasta em subpastas por extensão.
    Exemplo:
    - .txt -> txt/
    - .py -> py/
    """
    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"Pasta não encontrada: {folder_path}")

    # TODO: verificar cada item dentro da pasta
    # TODO: ignorar subpastas
    # TODO: criar subpastas por extensão
    # TODO: mover arquivos para suas pastas
    # TODO: retornar um resumo final
    pass


def task_summary(tasks):
    """
    Recebe uma lista de tarefas e retorna um resumo legível.
    Cada tarefa deve ter: titulo, status, descricao.
    """
    if not tasks:
        return "Nenhuma tarefa cadastrada."

    # TODO: contar tarefas por status
    # TODO: montar mensagem de resumo
    # TODO: retornar texto final
    pass


# Exemplo de uso:
# print(task_summary([
#     {"titulo": "Estudar Python", "status": "concluida", "descricao": "Revisar listas"},
#     {"titulo": "Praticar exercícios", "status": "pendente", "descricao": "Resolver 5 problemas"},
# ]))
# organize_files("./downloads")
