    # COMANDO ESCREVA

print('Mensagem a ser mostrada na tela, sempre entre aspas')

# Para juntar duas mensagens, pode-se usar a vírgular

print('Mensagem 1', 'Mesagem dois')

# Pode-se dar o comando para escrever um calculo

print(4+5)

    # ========DEFININDO VARIAVEIS===========

# Para definir uma variavel sempre usa-se o sinal de igual

variavel = 4 #variável sera igual a 4

# Para haver interação com o usuario, de modo que ele defina a váriavel usa-se o input

variavel2 = input('Digite uma variavel')

nome = input('Digite seu nome: ')

#Para substituir variaveis dentro de print, pode-se usar mascaras {}
    var = 'Mundo'
    print('Ola {}'.format(var))
        # ou
    var2 = input('Digite seu nome: ')
    filme = input('Qual filme voce quer ver: ')
    print('Ola {}, vamos assistir {}?'.format(var, filme))

# variaveis podem ser do tipo
    #str - texto
    #int - inteiro (4, -5, 0, 5546841)
    #float - ponto flutuante ou número real (5.0, 3.14, -444,5841)
    #bool - boleano verdadeirou ou falso (True or False) sempre em maisculo a primeira letra

# Pode-se checar qual o tipo da variavel usando o comando type

    type(variavel)

# Também pode-se verificar se a variavel é numerico, alfabetico, maiusculo, minusculo, se tem aspaços
# usando a função is

    n1 = input('Digite algo: ')
    print(n1.isalnum()) #se há letras ou números
    print(n1.isupper()) #se há maiusculas
    print(n1.islower()) #se há minusculas
    print(n1.isnumeric()) #se pode ser convertido em numero
    print(n1.isalpha()) #Se há letras
    print(n1.isnumeric()) #se pode ser convertido em numero
    print(n1.isspace()) #se há espaços
    #===========OPERADORES MATEMATICOS===========

# Para calculos se usa dois iguais, que significam igual.

    5+2 == 7 # Soma
    5-2 == 3 # Subtracao
    5*2 == 10 # Multriplicacao
    5/2 == 2.5 #Divisao
    5//2 == 2 # Modulo da divisao ou divisao inteira
    5%2 == 1 # Resto da divisao
    5**2 == 25 # Potenciacao

# A ordem de execucao de um calculo seguira:
        # (), potenciacao, mutiplicacao ou divisao ou resto ou modulo, subtracao ou adicao

# Pode-se fazer operacoes com str
    print('oi'*3) # resultado sera oioioi

# Para alinhar ou prrencher espacos pode-se usar {:}
a1 = input('Qual seu nome? ')
print('Seja bem vindo {:20}'.format(a1)) #escreve a variavel em 20 espacos
print('Seja bem vindo {:>20}'.format(a1)) #escreve a variavel em 20 espacos alinhado a esquerda
print('Seja bem vindo {:<20}'.format(a1)) #escreve a variavel em 20 espacos alinhado a direita
print('Seja bem vindo {:^20}'.format(a1))#escreve a variavel em 20 espacos alinhado a esquerda
print('Seja bem vindo {:=20}'.format(a1)) #escreve a variavel em 20 espacos com o sinal preenchendo

# para ajustar casas decimais pode-se usar {:.3f} le-se 3 casas decimais apos o ponto flutuante
    print('A soma e {:.5f}' .format(soma)) # 5 casas decimais

# pra quebrar a linha usa-se \n
    print('linha 1 \nlinha2')
# para nao quebrar a linha end=''
    print('linha1', end='')
    print('linha2')

#IMPORTAR MÓDULOS
    #adciona funcionalidades, bibliotecas
        #biblioteca math -> ceil, floor, trunc, pow, sqrt, factorial
import bebida # para importar todas as bebidas
from bebida import cerveja # #economiza memoria

# para encontrar mais bibliotecas padrões:
    #python.org > documentation > library references

# para encontrar bibliotecas da comunidade
    #python.org > pypi > procurar biblioteca > verificar cheat sheet da biblioteca
    # ou procurar e settings > project interpreter


