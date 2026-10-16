'''Crie uma função chamada processar_notas(lista_de_notas) que receba uma lista de números (representando notas de 0 a 10) e retorne um dicionário (ou imprima no console) contendo três informações:

    Aprovados: Uma nova lista contendo apenas as notas maiores ou iguais a 6.0.

    Reprovados: Uma nova lista contendo apenas as notas menores do que 6.0.

    Média da turma: A média aritmética de todas as notas fornecidas (com tratamento para caso a lista venha vazia).'''

notas = [10.0, 6.0, 7.0, 5.5, 4.5, 9.0]

def processar_notas(notas):

    notas_list = []
    soma_notas = sum(notas)
    tamanho_notas = len(notas)


    for count, nota in enumerate(notas, start=1):

        notas_dict = {}

        notas_dict['id'] = count
        notas_dict['nota'] = nota

        if nota >= 6.0:
        
            notas_dict['situação'] = 'aprovado'

        else:

            notas_dict['situação'] = 'reprovado'

        notas_dict['média da turma'] = soma_notas/tamanho_notas

        notas_list.append(notas_dict)

    return notas_list

print(processar_notas(notas))