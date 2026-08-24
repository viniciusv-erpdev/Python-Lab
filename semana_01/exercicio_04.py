# Dada uma lista de números, mostre apenas os números pares

numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    if numero%2 != 0:
        print("O número é impar: " + f"{numero}")
    else:
        print("O número é par: " + f"{numero}")