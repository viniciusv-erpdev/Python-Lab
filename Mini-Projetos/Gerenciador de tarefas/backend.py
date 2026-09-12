# Variáveis
task_dict = dict()

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

def create_task_dict(task_list):
    """Cria um dicionário com os dados recebidos do usuário.

    Recebe a lista de tarefas do usuário e associa com um id no dicionário
    
    Args:
        task_list: lista de tarefas
        task_dict: dicionário a ser criado

    Returns:
        O dicinário de tarefas"""

    id = 1

    task_dict = dict()

    task_dict[id] = task_list


    print(f'dicionário: {task_dict=}')
    
    return task_dict


def write_file(file_name, task_dict):

    with open(file_name, 'w', encoding='utf-8') as file:
        for item in task_dict:
            file.write(str(task_dict.values()))

    pass