'''Seção de estudos 22/09/2026
Assunto: Módulos'''

'''Em Python, conforme o tamanho do seus programas cresce, é uma boa prática seprar funções em arquivos diferentes.
Arquivos podem conter diferentes definições de classes, variáveis e funções. Os arquivos que compõem um script são conhecidos como módulos,
nomes de módulos seguem o padrão 'nome_do_modulo' seguido pela extensão .py. É possível invocar módulos dentro de outros módulos através do
comando import'''

# Exemplo de definição de uma função dentro do módulo 'modules_01.py'
# Esse módulo será importado dentro do módulo 'modules_01_exemplo.py'
def modulo_soma(a,b):

    return a + b

# Esse módulo será importado dentro do módulo 'modules_01_exemplo.py'
def modulo_mult(a,b):

    return a * b