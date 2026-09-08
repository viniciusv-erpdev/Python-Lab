# Seção de estudos dia 08/09/2026 - Assunto: arquivos

#====================================================
# MANIPULAÇÃO BÁSICA DE STRINGS
#====================================================

# Em python existem várias formas de demonstrar um output (originar uma informação), no início dos estudos uma forma comum é utilizar o comando print()
print("\n" + "1. Exemplo de output utilizando a função print()" + "\n")

# Outra forma comum pode ser utilizando f-strings
expression_number = 2
formatted_string_literals = "utilizando uma f-string"
print(f"{expression_number}. Exemplo de output {formatted_string_literals} \n")

# Pode-se controlar como strings se comportam com o método .format
# Exemplo utilizar duas casas decimais e porcentagem
yes_votes = 42572654
total_votes = 85705149
percentage = yes_votes/total_votes

print(f"Total de votos a favor {percentage: .2%} \n")

# Também é possível utilizar o método str() para representar qualquer valor como uma string exemplo:

number = 3
print(str(number) + ". Exemplo de str()" + "\n")

# Ao criar outpus é possível utilizar f-strings junto com o caractere ':' para delimitar um tamanho minímo de caracteres
# Isso é útil para criar colunas alinhadas
print("IMPRIMINDO UMA TABELA: " + "\n")
table = {"Vinicius": 10, "João": 9, "Maria": 8}
for nome, notas in table.items():
    print(f"{nome:10} ==> {notas:10}")

print("\n")

# Outro truque é utilizar o sinal "=" junto com f-strings para expandir expressões, isso é útil para debugs
nome_do_animal = "cachorro"

print(f"DEBUG {nome_do_animal=} \n")

# Você também pode inserir placeholders utilizando o método format()
print("Esse é um exemplo de {0}".format("format()") + "\n")