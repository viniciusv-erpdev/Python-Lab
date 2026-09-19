'''Seção de estudos 16/09/2026
Assunto: Exceptions e Erros'''

'''Implemente uma função de transferência bancária, que retorna erros caso as condições de transferência não sejam cumpridas'''

contas_bancarias = {
    "Alice": 1500.00,
    "Bob": 350.50,
    "Charlie":0.00
}

# Classe de exceção personalizada
class SaldoInsuficienteError(Exception):
    pass

def realizar_transferencia(origem, destino, valor):

    if origem not in contas_bancarias:

        raise KeyError(f'A conta de origem {origem=} não existe no sistema! \n')
    
    elif destino not in contas_bancarias:

        raise KeyError(f'A conta de destino {destino=} não existe no sistema! \n')

    elif valor <= 0:

        raise ValueError(f'O valor {valor=} não é valido para uma transferência, por favor tente novamente com um valor > 0! \n')

    if contas_bancarias.get(origem) < valor:

        raise SaldoInsuficienteError(f'O saldo da conta de origem {contas_bancarias.get(origem)=} é insuficiente para fazer a transferência de {valor=}!')

    for nome_conta in contas_bancarias:


        if nome_conta == origem:
            
            contas_bancarias[nome_conta] -= valor

        elif nome_conta == destino:

            contas_bancarias[nome_conta] += valor 

    return contas_bancarias

    

    

input_origem = input('Insira o nome da conta de origem: ')
input_destino = input('Insira o nome da conta de destino: ')
input_valor = float(input('Insira o valor da transferência: '))

print(realizar_transferencia(input_origem, input_destino, input_valor))