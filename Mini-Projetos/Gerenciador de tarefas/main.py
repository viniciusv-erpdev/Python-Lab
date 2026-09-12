import backend

print(f'insira os dados na ordem: descrição, prioridade, status \n')

def main():

    file_name = 'tasks_list.txt'

    description = input("Descrição: ")
    priority = input("Prioridade: ")
    status = input("Status: ")

    backend.create_file(file_name)

    task_list = backend.receive_data(description,priority,status)

    task_dict = backend.create_task_dict(file_name, task_list)

    backend.update_file(file_name, task_dict)
    
    
if __name__ == "__main__":
    main()