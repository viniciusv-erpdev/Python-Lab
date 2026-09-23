from seguranca import gerar_senha as gs
from seguranca import avaliar_forca as af

def main():

    while True:
        try:
            tamanho_senha = int(input("Digite o tamanho da senha: "))
            contem_pontuacao = int(input("Digite se a senha contém pontuação: (1 - Sim, 2 - Não)"))

            if contem_pontuacao != 1 and contem_pontuacao != 2:
                raise ValueError

            if type(tamanho_senha)!= int:
                raise ValueError

            if type(contem_pontuacao) != int:
                raise ValueError

            if tamanho_senha == 0:
                raise ValueError

            if contem_pontuacao == 1:
                senha_gerada = gs(tamanho_senha, True)

            if contem_pontuacao == 2:
                senha_gerada = gs(tamanho_senha, False)

            print(f'Senha gerada: {senha_gerada}')
            print(f'Força da senha {af(senha_gerada)}')

            break

        except ValueError:
            print("Valores inseridos inválidos")

        

if __name__ == "__main__":
    main()