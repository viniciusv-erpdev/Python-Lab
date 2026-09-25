'''Seção de estudos 24/09/2026
Assunto: Módulos'''

'''Exercício: Aprender a estruturar uma aplicação modularizada 
usando uma pasta/pacote customizada (estoque/), importando múltiplos 
submódulos e persistindo dados usando o módulo nativo json.'''

'''dados_produto = {
    'nome': 'Notebook',
    'quantidade': 4,
    'preco': 5000.00
}'''

# Calcula o preço total do inventário
def calcular_valor_total(inventario):

    total = 0.00

    for items in inventario:
        total += items['preco'] * items['quantidade']

    return total

# Exibir inventário
def exibir_resumo(inventario):

    print(f'\n---RESUMO DO INVENTÁRIO---\n')
    
    for counter, item in enumerate(inventario, start=1):
        nome = item['nome']
        quantidade = item['quantidade']
        preco = item['preco']
        subtotal = quantidade * preco
        print(f'{counter} - {nome} | Qntd: {quantidade} | Preço: R${preco:.2f} | Subtotal: R${subtotal:.2f}')
        print(f'------\n')
        


