# Crie uma função que abra e leia um arquivo de texto, 
# conte o número total de linhas presentes no arquivo,
# filtre apenas as linhas que contem a palavra_chave, 
# escreva as linhas filtradas em um novo arquivo chamado arquivo_destino
# a função deve retornar o total de linhas do arquivo original e quantas linhas foram salvas no arquivo ex: [10,3]

def processar_relatorio(arquivo_origem, arquivo_destino, palavra_chave):

    qntd_linhas = 0
    qntd_linhas_escritas = 0
    linhas_palavra_chave = []
    total_original_e_salvas_no_arquivo = []

    with open(arquivo_origem, 'r', encoding='utf-8') as file:

        for counter, line in enumerate(file, start=1):

            matching_lines = line.lower()
            matching_key_words = palavra_chave.lower()

            if matching_key_words in matching_lines:
                linhas_palavra_chave.append(line)

            qntd_linhas = counter

    with open(arquivo_destino, 'w', encoding='utf-8') as new_file:

        print(f'{linhas_palavra_chave=}')

        for counter, line in enumerate(linhas_palavra_chave, start=1):

            new_file.write(f'{line}')

            qntd_linhas_escritas = counter

    total_original_e_salvas_no_arquivo.append(qntd_linhas)
    total_original_e_salvas_no_arquivo.append(qntd_linhas_escritas)

    return total_original_e_salvas_no_arquivo

total, salvas = processar_relatorio('log.txt', 'erros_encontrados.txt', 'ERROR')
print(f"Total de linhas lidas: {total}")
print(f"Linhas de erro salvas: {salvas}")