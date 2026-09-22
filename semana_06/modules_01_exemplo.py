'''Seção de estudos 22/09/2026
Assunto: Módulos'''

# A palavra import seguida pelo nome do módulo permite que você utilize-o dentro de outro script.
import modules_01

# Também é possível importar apenas funções ou classes de outros módulos.
from modules_01 import modulo_mult

# Além disso, pode-se importar um módulo definindo-o como uma palavra chave, utilizando o comando 'as'.
import modules_01 as primeiro_mod

# Módulo importado do arquivo anterior

print(modules_01.modulo_soma(2,5))

print(modulo_mult(3,3))

print(primeiro_mod.modulo_soma(2,2))

# O comando dir pode ser utilizado para mostrar os nomes definidos em um módulo.
print(dir(modules_01))

'''Por último, Python possui alguns módulos 'padrões' já incluídos em seu interpretador, utilizados 
para complementar funcionalidades da linguagem, como por exemplo o módulo sys pode ser utilizado
para acessar comandos do sistema operacional.'''