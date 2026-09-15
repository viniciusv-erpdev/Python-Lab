'''Seção de estudos 15/09/2026
Assunto: Exceptions e Erros'''

'''Breve resumo:
Exceptions são um dos dois tipos distinguíveis de erros no Python, sendo eles:
Parse errors: são erros tratados pela linguagem de programação quando há algum problema na execução de uma parte do código, eles interompem a execução do mesmo.
Exception errors: São erros tratados pelo programador, geralmente retornam alguma mensagem personalizada e não quebram o fluxo de execução do programa.'''

'''Exemplos'''
#Exception errors:
while True:
    try:
        x = int(input())
        break
    except ValueError:
        print('Este valor não é um número')


#Parse errors:
#while True print('Hello World!')