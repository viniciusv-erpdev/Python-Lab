'''Seção de estudos 23/09/2026
Assunto: Módulos'''

'''Exercício: praticar a utilização de módulos através de um gerador de senhas'''

# Imports
import random
import string

def gerar_senha(tamanho, usar_especiais):

    #variáveis
    i = 0
    lista_auxiliar_caracteres = []

    # Gera uma string com valores aleatórios da lista ascii
    if usar_especiais == False:

        senha = ''.join(random.choices(string.ascii_letters, k=tamanho))

    # Gera uma lista com caracteres e pontuação caso usar_especiais seja verdadeiro
    if usar_especiais == True:

        while i < tamanho:

            i += 1

            if i < (tamanho // 2):

                lista_auxiliar_caracteres.append(''.join(random.choices(string.ascii_letters, k=1)))

            else:

                lista_auxiliar_caracteres.append(''.join(random.choices(string.punctuation, k=1)))

        senha = ''.join(random.sample(lista_auxiliar_caracteres, k=tamanho))

    return senha

def avaliar_forca(senha):

    caracteres_letras = string.ascii_letters
    caracteres_pontuacao = string.punctuation

    if len(senha) < 8:
        return 'Fraca'

    if len(senha) >= 8 and not any(c in senha for c in caracteres_pontuacao):
        return 'Média'

    if len(senha) >= 8 and any(c in senha for c in caracteres_letras) and any(c in senha for c in caracteres_pontuacao):
        return 'Forte'
