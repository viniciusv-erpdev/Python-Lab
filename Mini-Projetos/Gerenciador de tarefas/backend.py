# Imports
import os
from pathlib import Path
import json

output_file = 'tasks_list.json'

def create_file(file_name):

    '''Cria um novo arquivo 'tasks_list.txt' se ele não existir 
    
    Args: 
        file_name: string - nome do arquivo'''

    if Path(file_name).exists() == False:
        Path(file_name).touch()
        print(f'Arquivo criado com sucesso! \n')

def receive_data(task_id, description, priority, status):
    """Recebe os dados das tarefas pelos usuários.

    Recebe o input de dados para cada tarefa enviado pelo usuário e retorna
    uma lista com todos os dados
    
    Args:
        description: string - descrição da tarefa
        priority: string - prioridade da tarefa
        status: string - status da tarefa

    Returns:
       A lista com os dados inseridos pelo usuário"""

    new_task_dict = {}
    new_task_list = []

    new_task_dict['id'] = task_id
    new_task_dict['descrição'] = description
    new_task_dict['prioridade'] = priority
    new_task_dict['status'] = status

    new_task_list.append(new_task_dict)

    return new_task_list

def read_file(file_name):
    """Lê o arquivo .json gerado e armazena seu conteúdo em uma lista
    e retorna a lista
    
    Args:
        file_name: string - nome do arquivo

    Returns:
       A lista com os dados do arquivo .json"""
    file_task_list = []

    if os.path.getsize(file_name) == 0:
        return file_task_list

    with open(file_name, 'r', encoding='utf-8') as file:

        file_task_list = json.load(file)

    return file_task_list

        
def generate_full_list(file_name, new_data_list):
    """Recebe o nome do arquivo já existente e os novos dados a serem
    gravados na iteração. Concatena os dois dados em uma única lita e a retorna.
    
    Args:
        file_name: string - nome do arquivo
        new_data_list: list - lista com o novo dicionário de dados da iteração

    Returns:
       uma lista unificada com todos os dados"""

    
    existing_data = read_file(file_name)

    full_list = existing_data + new_data_list

    return full_list

def atributte_task_id(file_tasks_list):
    
    maior_task_id = 0

    if not file_tasks_list:
        return 0  

    else:

        for task in file_tasks_list:

            current_task_id = task['id']

            if current_task_id > maior_task_id:

                maior_task_id = current_task_id

    return maior_task_id + 1

    
def record_file(file_name, task_list):
    """Recebe o nome do arquivo e uma lista com as tarefas e armazena os dados
    das tarefas em um arquivo de formato .json
    
    Args:
        file_name: string - nome do arquivo
        task_list: string - dados das tarefas"""

    
    create_file(output_file)

    with open(file_name, 'w', encoding='utf-8') as file:

        json.dump(task_list, file, indent=2, ensure_ascii=False)

def update_task(task_id, complete_task_list):

    for task_dict in complete_task_list:

        if task_dict['id'] == task_id:

            input_desc = input(f'Alterar descrição {task_dict['descrição']}: ')
            input_priority = input(f'Alterar prioridade {task_dict['prioridade']}: ')
            input_status = input(f'Alterar status{task_dict['status']}: ')

            task_dict['descrição'] = input_desc
            task_dict['prioridade'] = input_priority
            task_dict['status'] = input_status

            break

    return complete_task_list

def delete_task(task_id, complete_task_list):

    for task_dict in complete_task_list:

        if task_dict['id'] == task_id:

            complete_task_list.remove(task_dict)

            break

    return complete_task_list

#!!! Testes backend
create_file(output_file)

existing_tasks = read_file(output_file)
task_id = atributte_task_id(existing_tasks)
new_tasks_list = receive_data(task_id, 'teste', 'teste', 'teste')
complete_task_list = generate_full_list(output_file, new_tasks_list)

record_file(output_file, complete_task_list)

new_list = update_task(0, complete_task_list)
print(new_list)

record_file(output_file, new_list)