import backend

print(f'insira os dados na ordem: descrição, prioridade, status \n')

def main():

    file_name = 'tasks_list.txt'

    description = input("Descrição: ")
    priority = input("Prioridade: ")
    status = input("Status: ")

    task_list = backend.receive_data(description,priority,status)

    task_dict = backend.create_task_dict(task_list)

    backend.write_file(file_name, task_dict)
    
    
if __name__ == "__main__":
    main()