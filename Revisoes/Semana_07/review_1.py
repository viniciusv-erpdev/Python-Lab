'''Escreva um código em Python que:

    1 - Percorra a lista de novos itens.

    2 - Se o produto já existir no dicionário de estoque, some a nova quantidade à quantidade existente.

    3 - Se o produto não existir no dicionário, adicione-o ao dicionário com a quantidade informada.'''

estoque = {
    "camiseta": 15,
    "calça": 8,
    "tênis": 5
}

novas_entradas = [
    ("camiseta", 10),
    ("boné", 12),
    ("calça", 5),
    ("meia", 20),
    ("tênis", 3)
]

def atualizar_dict(novas_entradas):

    for item in novas_entradas:

        if item[0] not in estoque:

            estoque[item[0]] = item[1]

        else:

            estoque[item[0]] += item[1]

    return estoque

print(atualizar_dict(novas_entradas))
         