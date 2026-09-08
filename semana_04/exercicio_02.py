# Seção de estudos dia 08/09/2026 - Assunto: arquivos

#====================================================
# MANIPULAÇÃO BÁSICA DE ARQUIVOS
#====================================================

# Em Python, podemos ler arquivos utilizando o método open() ele retorna um object file
# Geralmente open é utilizado com dois positional arguments e um keyword argument

# open('workfile.txt', 'r+', encoding='utf-8')

# No exemplo a cima:
# workfile.txt é o nome do arquivo a ser aberto
# r+ significa que o arquivo será aberto em modo de leitura e edição
# encoding='utf-8' por enquanto pode ser entendido como a forma como o arquivo será 'traduzido' pelo Python utf-8 geralmente é o encoding mais utilizado

# por padrão arquivos em Python são abertos e escritos na forma de strings o que significa que o Python vai ler e escrever em formato string
# é possível fazer um append 'b' para o modo de abertura do arquivo, que significa que o Python irá ler e escrever em bytes utilizando formato binário

# Ao ler arquivos geralmente é especificado o caractere \n para delimitar quebras de linhas 
# Ao escrever em arquivos o padrão é converter \n de volta para a quebra de linhas específica da plataforma

# Escrever em arquivos conténdo JPEG´s ou EXE´s pode corromper o arquivo

# Existem duas formas mais comuns de abrir arquivos:
# try-finally
# with (Por enquanto, focaremos nela pois é mais curta e fecha o arquivo automaticamente após a operação)
with open('workfile.txt', encoding='utf-8') as f:
    read_data = f.read()
    print(read_data)

print("\n")

# O método read(size) tem como argumento a quantidade de leitura desejada
# Esse argumento não é obrigatório, no entanto, deve-se atentar pois um arquivo pode possuir um tamanho de dados superior a memória de sua máquina

# Podemos verificar se o arquivo foi fechado após sua utilização
verify = f.closed
print(f"{verify=} \n")

# Se não utilizar o comando with o arquivo deve ser fechado através do método f.close(), isso garante que o programa não faça uso desnecessário dos recursos do sistema

with open('workfile.txt', encoding='utf-8') as f:
    for i in range(3):
        print(f'{i}. ' + f.readline())

print("\n")

# O método readline é utilizado para ler uma única linha do arquivo, ele para no caractere utilizado para quebrar a linha geralmente '\n'
# Quando ele retorna '' significa que o arquivo chegou ao fim

with open('workfile.txt', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

print("\n")

# É possível percorrer linha por linha de um arquivo fácilmente utilizando um loop for

with open('workfile.txt', 'a+', encoding='utf-8') as f:
    f.write('Python wrote this!')

    for line in f:
        print(line, end='')

# Também é possível escrever no arquivo utilizando o método write
# No exemplo a cima abrimos o arquivo no modo append+, o que significa que o novo texto escrito pelo método write será adicionado ao texto já existente no documento