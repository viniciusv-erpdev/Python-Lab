'''Seção de estudos 22/09/2026
Assunto: Módulos'''

'''Exercício: praticar a utilização de módulos através de um simples programa de gestão financeira 
dividido em mais de um script.'''

def calcular_imposto(valor, taxa=0.15):

    valor_imposto = valor * taxa

    return valor_imposto

def formatar_moeda(valor):

    valor_auxiliar = str(valor).replace('.',',')

    moeda_formatada = str(f'R$ {valor_auxiliar}')

    return moeda_formatada

def resumo_transacao(valor, taxa=0.15):

    valor = float(valor)

    valor_imposto = calcular_imposto(valor)

    valor_liquido = valor - valor_imposto

    valor_bruto = formatar_moeda(valor)

    valor_imposto_convertido = formatar_moeda(valor_imposto)

    valor_liquido_convertido = formatar_moeda(valor_liquido)

    print(f'--- Resumo da Transação ---')
    print(f'Valor bruto: {valor_bruto}')
    print(f'Imposto: {valor_imposto_convertido}')
    print(f'Valor líquido: {valor_liquido_convertido}')
    print(f'----------------------------')

    

