# Imports
import os
from pathlib import Path

# Variáveis
task_dict = dict()
file_path = "tasks_list.txt"

def receive_data(description, priority, status):
    """Recebe os dados das tarefas pelos usuários.

    Recebe o input de dados para cada tarefa enviado pelo usuário e retorna
    uma lista com todos os dados
    
    Args:
        description: string - descrição da tarefa
        priority: string - prioridade da tarefa
        status: string - status da tarefa

    Returns:
        A lista de dados inseridos pelo usuário"""

    task_list = []

    task_list.append(description)
    task_list.append(priority)
    task_list.append(status)
    
    return task_list

def create_file(file_name):

    '''Cria um novo arquivo 'tasks_list.txt' se ele não existir '''

    if Path(file_name).exists() == False:
        Path(file_name).touch
        print(f'Arquivo criado com sucesso! \n')


def create_task_dict(file_name, task_list):
    """Cria um dicionário com os dados recebidos do usuário.

    Recebe a lista de tarefas do usuário e associa com um id no dicionário
    
    Args:
        file_name: nome do arquivo
        task_dict: dicionário a ser criado

    Returns:
        O dicinário de tarefas"""

    id = 0

    if Path('tasks_list.txt').exists():
        
        with open(file_name, 'r', encoding='utf-8') as f:

            # Caso o arquivo esteja vazio
            if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
                id = 0

            for line in f:

                id += 1

    else:

        print("Erro o arquivo tasks_list.txt não foi encontrado")

    task_dict[id] = task_list


    print(f'dicionário: {task_dict=}')
    
    return task_dict

def update_file(file_name, task_dict):

    """Adiciona linhas a um arquivo com base no dicionário de dados.

    Recebe o nome do arquivo e o dicionário e escreve um arquivo
    com os dados do dicionário
    
    Args:
        file_name: Nome do arquivo
        task_dict: Dicionário de tarefas"""

    with open(file_name, 'a', encoding='utf-8') as file:

        for id, item in task_dict.items():

            # Caso o arquivo esteja vazio
            if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
                file.write(f'{id}, {item}')

            if os.path.isfile(file_path) and os.path.getsize(file_path) != 0:
                file.write(f'\n{id}, {item}')

    pass