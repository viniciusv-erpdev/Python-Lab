'''Seção de estudos 15/09/2026
Assunto: Exceptions e Erros'''

'''Exercício: Crie um script que solicite ao usuário nome de um arquivo com notas dos alunos e retorne erros caso a lista esteja vazia ou possua notas não numéricas'''
from pathlib import Path

def calcular_media_alunos(notas):

    lista_notas = []

    with open(notas, 'r', encoding='utf-8') as file:

        file_path = Path(notas)

        try:
            if file_path.is_file() and file_path.stat().st_size == 0:
                raise ValueError()
        except ValueError:
            return print(f'Erro arquivo vazio')

        
        for line in file:
            lista_notas.append(line.strip('\n'))

    try:
        for counter, nota in enumerate(lista_notas, start=0):

            lista_notas[counter] = float(nota)

            if lista_notas[counter] > 10.0:
                raise ValueError()
            
    except ValueError:
        return print(f'Nota inválida encontrada: {nota=}. Deve ser um número entre 1 e 10.')

    media_nota = sum(lista_notas)/len(lista_notas)

    return media_nota

nome_do_arquivo = input()

print(calcular_media_alunos(nome_do_arquivo))