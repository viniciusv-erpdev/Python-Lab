'''Seção de estudos 18/09/2026
Assunto: Exceptions e Erros'''

# Implemente uma função para validar compras em um e-commerce, lançando erros caso as compras falhem

# Dados
clientes = {
    "101": {"nome": "Lucas", "ativo": True, "saldo": 250.00},
    "102": {"nome": "Mariana", "ativo": False, "saldo": 500.00},
    "103": {"nome": "Carlos", "ativo": True, "saldo": 30.00}
}

estoque = {
    "P01": {"nome": "Teclado", "preco": 120.00, "qtd": 5},
    "P02": {"nome": "Mouse", "preco": 50.00, "qtd": 0},
    "P03": {"nome": "Monitor", "preco": 800.00, "qtd": 2}
}

class ClienteInativoError(Exception):
    pass

class EstoqueInsuficienteError(Exception):
    pass

def processar_pedido(cliente_id, produto_id, quantidade):

    # verifica se o id do cliente existe no dicionário de clientes
    if cliente_id not in clientes:
    
        raise KeyError(f'O cliente {cliente_id=} não existe no sistema!')

    # verifica se o id do produto existe no dicionário de estoque
    if produto_id not in estoque:

        raise KeyError(f'o produto {produto_id=} não existe no sistema!')

    # verifica se o cliente está ativo
    if clientes[cliente_id].get('ativo') == False:
        raise ClienteInativoError(f'O cliente {cliente_id=} está inativo no sistema!')

    # verifica se a quantidade do pedido for menor ou igual a zero
    if quantidade <= 0.0:

        raise ValueError(f'A quantidade do pedido {quantidade=} é inválida. Insira um valor maior que 0')

    # verifica se a quantidade verificada não é maior do que o estoque disponível
    quantidade_disponivel = estoque[produto_id].get('qtd')

    if quantidade > quantidade_disponivel:

        raise EstoqueInsuficienteError(f'O estoque do produto não é suficiente para satisfazer a compra! {quantidade_disponivel=}')

    # verifica se o cliente tem saldo o suficiente para realizar a transação

    saldo_cliente = clientes[cliente_id].get('saldo')
    preco_produto = estoque[produto_id].get('preco')

    if saldo_cliente < preco_produto * quantidade:

        raise ValueError(f'O saldo do cliente {saldo_cliente=} não é o suficiente para completar a transação!')

    estoque[produto_id]['qtd'] -= quantidade
    clientes[cliente_id]['saldo'] -= (preco_produto * quantidade)
    
    pass

id_cliente = input('Digite o id do cliente: ')
id_produto = input('Digite o id do produto: ')
quantidade = float(input('Digite a quantidade a ser comprada: '))

try:

    processar_pedido(id_cliente, id_produto, quantidade)

except KeyError as e:
    print(f'\n[Erro de cliente invalido]: {e if str(e) else 'insira apenas quantidades válidas.'}')

except ClienteInativoError as e:
    print(f'\n[Erro de cliente inativo] {e}')

except ValueError as e:
    print(f'\n[Erro de Valor] {e}')

except EstoqueInsuficienteError as e:
    print(f'\n[Erro de quantidade de estoque] {e}')

else:

    print(f'Transação realizada com sucesso!')

print(estoque)
print('\n')
print(clientes)