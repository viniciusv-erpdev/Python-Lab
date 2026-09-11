# Exercícios dia 11/09/2026

# ====================
# Revisão sem consulta
# ====================

# Assunto manipulação de arquivos

# Exercício 1) conte quantas palavras e quantas linhas aparecem no arquivo discurso_obama.txt

def file_counter(file_name):

    number_of_lines = 0
    words = 0
    list_lines_words = []

    with open(file_name, 'r', encoding='utf-8') as file:

        for counter, lines in enumerate(file, start=1):

            number_of_lines = counter

            words += len(lines.split())


        list_lines_words.append(f'Número de linhas: {number_of_lines}')
        list_lines_words.append(f'Número de palavras: {words}')
        
    return list_lines_words

print(file_counter('discurso_obama.txt'))


