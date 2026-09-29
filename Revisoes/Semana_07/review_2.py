'''Escreva uma função em Python chamada calcular_running_max(temperaturas) que:

    1- Receba uma lista de números (temperaturas).

    2- Percorra a lista mantendo o registro do maior valor encontrado até o momento.

    3- Retorne uma nova lista contendo o maior valor atualizado a cada dia.'''

temperaturas = [22, 25, 19, 28, 24, 31, 29, 31, 35, 30]

def calcular_running_max(temperaturas):

    maior_temperatura = temperaturas[0]

    for temperatura in temperaturas:

        if temperatura > maior_temperatura:

            maior_temperatura = temperatura

    return maior_temperatura

print(calcular_running_max(temperaturas))
