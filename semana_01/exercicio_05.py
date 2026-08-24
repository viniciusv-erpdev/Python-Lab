# Dada uma lista de notas, calcule quantos alunos foram aprovados considerando nota >= 7

notas = [10.0, 6.0, 7.5, 8.0, 9.5, 5.0, 4.5, 2.5, 8.5]

contador = 0

for nota in notas:
    if nota >= 7:
        contador = contador + 1

print("A quantidade de alunos que foram aprovados com nota maior ou igual a 7 é de: " + f"{contador}")