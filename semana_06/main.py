'''Seção de estudos 22/09/2026
Assunto: Módulos'''

'''Exercício: praticar a utilização de módulos através de um simples programa de gestão financeira 
dividido em mais de um script.'''

from financeiro import formatar_moeda, calcular_imposto, resumo_transacao

# alternativa
from financeiro import formatar_moeda as fmt

def main():

    

    while True:
        try:
            valor = input('insira o valor desejado: ')
            float(valor)
            resumo_transacao(valor)
            break
        except Exception:
            print('Ocorreu um erro inesperado ao executar o programa, por favor verifique os valores inseridos e tente novamente.')

    pass

if __name__ == "__main__":
    main()