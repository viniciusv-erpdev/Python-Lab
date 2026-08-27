# Revisão de loops

numeros = [15, 3, 28, 7, 42, 9, 18]

# 1. Maior número de uma lista

contador_elementos = 0
maior_numero = numeros[0]
menor_numero = numeros[0]

for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

    if numero < menor_numero:
        menor_numero = numero

    contador_elementos += 1

print("O maior número da lista é: " + f"{maior_numero}" + "\n")
print("O maior número da lista é: " + f"{menor_numero}" + "\n")

# 2. A soma dos elementos da lista
print("A lista possui: " + f"{contador_elementos}" + " elementos." + "\n")

# Ou

print("A lista possui: " + f"{len(numeros)}" + " elementos." + "\n")

# 3. A média da lista
print("A média da lista é: " + f"{(sum(numeros)/len(numeros))}" + "\n")

# Exercício 07
notas = [8.5, 6.0, 9.2, 4.5, 7.0, 5.8, 10.0]

contador_alunos = 0
alunos_aprovados = 0
alunos_reprovados = 0
maior_nota = notas[0]
menor_nota = notas[0]

# 1. Quantidade de alunos
# 2. Quantidade de aprovados
# 3. Quantidade de reprovados
# 4. Maior nota
# 5. Menor nota
for nota in notas:
    contador_alunos += 1

    if nota > maior_nota:
        maior_nota = nota

    if nota < menor_nota:
        menor_nota = nota

    if nota >= 7.0:
        alunos_aprovados += 1
    else:
        alunos_reprovados += 1


print("A quantida de alunos é: " + f"{contador_alunos}" + "\n")
print(f"{alunos_aprovados}" + " Alunos foram aprovados!" + "\n")
print(f"{alunos_reprovados}" + " Alunos foram reprovados!" + "\n")
print("A maior nota foi: " + f"{maior_nota}" "\n")
print("A menor nota foi: " + f"{menor_nota}" "\n")
