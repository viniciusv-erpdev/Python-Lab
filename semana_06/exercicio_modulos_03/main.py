'''Seção de estudos 25/09/2026
Assunto: Módulos'''

'''Exercício: Aprender a estruturar uma aplicação modularizada 
usando uma pasta/pacote customizada (estoque/), importando múltiplos 
submódulos e persistindo dados usando o módulo nativo json.'''

'''dados_produto = {
    'nome': 'Notebook',
    'quantidade': 4,
    'preco': 5000.00
}'''

# Imports
from estoque import produtos
from estoque import relatorio

def main():

    inventario = []

    # Carrega o inventário
    inventario_auxiliar = produtos.carregar_inventario()

    # Adiciona produtos
    produtos.adicionar_produto(inventario, 'Notebook', 5, 3500.00)
    produtos.adicionar_produto(inventario, 'Teclado', 10, 50.00)
    produtos.adicionar_produto(inventario, 'mouse', 3, 20.00)

    # Salva inventário no arquivo
    produtos.salvar_inventario(inventario)

    # Exibe inforamções do inventário
    print(relatorio.exibir_resumo(inventario_auxiliar))

    # Mostra o valor total do inventário
    print(f'Valor Total do inventário: {relatorio.calcular_valor_total(inventario_auxiliar)}')

if __name__ == '__main__':
    main()