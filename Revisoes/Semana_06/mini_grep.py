import os

class ErroDeGrep(Exception):
    pass

class ErroTermoInexistente(Exception):
    pass

def procura_termo(arquivo, termo_procurado, flag):

    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, arquivo)
    contador_correspondencias = 0
    lista_correspondencia = []

    print(f'\nArquivo: {arquivo}')
    print(f'\nPesquisar: {termo_procurado}\n')

    if os.path.isfile(caminho_arquivo) == False:

        raise ErroDeGrep(f'\n O arquivo {arquivo} não existe no diretório atual! \n')
    
    with open(arquivo, 'r', encoding='utf-8') as arquivo_aberto:

        for contador, linha in enumerate(arquivo_aberto, start=1):

            linha_auxiliar = linha
            termo_auxiliar = termo_procurado

            if 'm' in flag:

                linha_auxiliar = linha_auxiliar.lower()
                termo_auxiliar = termo_auxiliar.lower()

            busca_encontrada = (termo_auxiliar in linha_auxiliar)

            if busca_encontrada == True:

                contador_correspondencias += 1
                    
                if 'n' not in flag:

                    print(f'[{contador}] {linha}')

                lista_correspondencia.append(linha)

    if contador_correspondencias == 0:

        raise ErroTermoInexistente(f'\nO termo: {termo_procurado} não existe no arquivo!\n')

    with open('resultados.txt', 'w', encoding='utf-8') as arquivo_escrito:

        for linha in lista_correspondencia:
            arquivo_escrito.write(linha)

    print(f'\nTotal: {contador_correspondencias} Linhas encontradas.\n')
    

    return(f'\nFunção executada com sucesso!\n')


while True:

    try:
        nome_arquivo = input(f'\nPor Gentileza informe o nome do arquivo: \n')
        nome_termo = input(f'\nPor gentileza informe qual o termo a ser encontrado no arquivo: \n')
        flag = input(f'\nPor gentileza informe as flags de processamento\n')
        execucao_grep = procura_termo(nome_arquivo, nome_termo, flag)
        print(execucao_grep)

    except ErroDeGrep as e:

        print(f'\n [ERRO AO PROCURAR ARQUIVO]: {e} \n')

    except ErroTermoInexistente as e:
    
            print(f'\n [ERRO PESQUISA INEXISTENTE]: {e} \n')

    else: 

        break


