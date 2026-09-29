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

def receive_data(description, priority, status):
    """Recebe os dados das tarefas pelos usuários.

    Recebe o input de dados para cada tarefa enviado pelo usuário e retorna
    uma lista com todos os dados
    
    Args:
        description: string - descrição da tarefa
        priority: string - prioridade da tarefa
        status: string - status da tarefa

    Returns:
       A lista com os dados inseridos pelo usuário"""

    task_dict = {}
    task_list = []

    task_dict['descrição'] = description
    task_dict['prioridade'] = priority
    task_dict['status'] = status

    task_list.append(task_dict)

    return task_list

def read_file(file_name):

    file_task_list = []
    
    if os.path.getsize(file_name) == 0:
        return file_task_list

    with open(file_name, 'r', encoding='utf-8') as file:

        for line in file:

            file_task_list.append(line.strip('\n'))

    return file_task_list

def record_file(file_name, task_list):

    create_file(output_file)

    with open(file_name, 'r+', encoding='utf-8') as file:

        for task in tasks_list:
            json.dump(task_list, file, indent=2, ensure_ascii=False)


#!!! Testes backend
create_file(output_file)

tasks_list = receive_data('teste', 'teste', 'teste')

record_file(output_file, tasks_list)        

print(read_file(output_file))
        


    