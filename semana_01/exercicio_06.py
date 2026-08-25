# Exercício A. Mostre somenta as idades maiores ou iguais a 18
idades = [18, 21, 17, 32, 25, 16, 40]

for idade in idades:
    if idade >= 18:
        print(idade)

print('\n')

# Exercício B. Dada a mesma lista, descubra quantas pessoas são maiores ou iguais a 18
idade_contador = 0

for idade in idades:
    if idade >= 18:
        idade_contador = idade_contador + 1

print("O total de pessoas maiores de idade é de: " + f"{idade_contador}" + "\n")

# Exercício C

numeros = [3, 8, 12, 7, 15, 20, 21, 30]

# 1. Mostrar os números pares
for numero in numeros:
    if numero%2 == 0:
        print("Números pares: " + f"{numero}")

print("\n")

# 2. Contar quantos números pares existem
numeros_contador = 0

for numero in numeros:
    if numero%2 == 0:
        numeros_contador = numeros_contador + 1

print("Existem: " + f"{numeros_contador}" + " números pares" + "\n")

# Exercício D. 

notas = [8.5, 6.0, 9.2, 4.5, 7.0, 5.8, 10.0]

contador_aprovados = 0
contador_reprovados = 0

# 1. Quantos alunos foram aprovados (>=7) e quantos foram reprovados (<7)
for nota in notas:
    if nota >= 7:
        contador_aprovados = contador_aprovados + 1
    else:
        contador_reprovados = contador_reprovados + 1

print(f"{contador_aprovados}" + " alunos foram aprovados!" + "\n")
print(f"{contador_reprovados}" + " alunos foram reprovados!" + "\n")

# 2. Qual a maior e a menor nota

maior_nota = notas[0]
menor_nota = notas[0]

for nota in notas:
    if nota > maior_nota:
        maior_nota = nota

    if nota < menor_nota:
        menor_nota = nota

print("A maior nota é: " + f"{maior_nota}")
print("A menor nota é: " + f"{menor_nota}")

print("\n")

# Desafio. Exibe os preços acima de 100 e descobra quantos produtos estão nessa situação

precos = [50, 120, 80, 250, 99, 175, 40, 300]

qntd_produtos = 0

for preco in precos:
    if preco > 100:
        print("Preços maiores que 100: " + f"{preco}")
        qntd_produtos = qntd_produtos + 1

print("Quantidade de produtos com preço maior que 100: " + f"{qntd_produtos}")

