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

# Import do módulo nativo JSON
import json
from pathlib import Path

# Variáveis
pasta_destino = Path(__file__).parent

# Adiciona um dicionário de informações do produto em uma lista
def adicionar_produto(inventario, nome, quantidade, preco):

    dados_produto = {
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco
    }
        
    inventario.append(dados_produto)

    return ('Produtos salvos com sucesso!')

# Salva o conteúdo da lista em um arquivo .json
def salvar_inventario(inventario, arquivo= pasta_destino / 'inventario.json'):

    with open(arquivo, 'w') as file:

        json.dump(inventario, file, indent=4)

    return('Inventário gravado com sucesso!')

# lê o arquivo .json e armazena-o em uma lista
def carregar_inventario(arquivo='inventario.json'):

    pasta_atual = Path(__file__).parent
    arquivo_atual = pasta_atual / arquivo
    lista_auxiliar_leitura = []

    if not arquivo_atual.exists():
        return lista_auxiliar_leitura

    with open(arquivo_atual, 'r') as file:
        return json.load(file)
