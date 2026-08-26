# Estudos sobre while

# Imprima i enquanto i for menor que 6
i = 0
while i < 6:
    i += 1

print(i)
print("\n")

# Break pode ser utilizado para quebrar um loop while

n = 0
while n < 6:
    n += 1
    if n == 3:
        break

print(n)
print("\n")

# Continue pode ser utilizado para continuar para próxima iteração
j = 0
while j < 6:
    j += 1
    if j == 3:
        continue

print(j)
print("\n")

# Podemos utilizar o else junto com o while
p = 0
while p < 6:
    p += 1
else:
    print("p não é menor que 6" + "\n")