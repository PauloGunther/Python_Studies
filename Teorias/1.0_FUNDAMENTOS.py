# COMANDO ESCREVA

print('Mensagem a ser mostrada na tela, sempre entre aspas')

# Para juntar duas mensagens, pode-se usar a vírgular
print('Mensagem 1', 'Mesagem dois')

# Pode-se dar o comando para escrever um calculo
print(4+5)

# DEFININDO VARIAVEIS

# Para definir uma variavel sempre usa-se o sinal de igual
variavel = 4  # valor 4 esta armazenado na variavel

# Para haver interação com o usuario, de modo que ele defina a váriavel usa-se o input
variavel2 = input('Digite uma variavel')
nome = input('Digite seu nome: ')

# Para substituir variaveis dentro de print, pode-se usar mascaras {}
var = 'Mundo'
print('Ola {}'.format(var))  # Para isso usa-se o .format()

var2 = input('Digite seu nome: ')  # primeira variavel
filme = input('Qual filme voce quer ver: ')  # segunda variavel
print('Ola {}, vamos assistir {}?'.format(var, filme))  # cada mascara recebera a variavel dentro do format em ordem

# TIPOS DE VARIAVEIS

#    str - texto - leia-se string
#   int - inteiro (4, -5, 0, 5546841) - leia-se integer
#   float - ponto flutuante ou número real (5.0, 3.14, -444,5841)
#   bool - boleano verdadeirou ou falso (True or False) sempre em maisculo a primeira letra

# Pode-se checar qual o tipo da variavel usando o comando type
print(type(variavel))  # ira printar o tipo de variavel

# Também pode-se verificar se a variavel é numerico, alfabetico, maiusculo, minusculo, se tem aspaços
# usando a variavel.is
n1 = input('Digite algo: ')
print(n1.isalnum())  # se há letras ou números
print(n1.isupper())  # se as letras sao todas maiusculas
print(n1.islower())  # se as letras sao todas minusculas
print(n1.isnumeric()) # se pode ser convertido em numero (inteiro ou float)
print(n1.isalpha())  # Se há letras
print(n1.isspace())  # se é um espaço


# OPERADORES MATEMATICOS

5+2 == 7  # Soma
5-2 == 3  # Subtracao
5*2 == 10  # Multriplicacao
5/2 == 2.5  # Divisao
5//2 == 2  # Modulo da divisao ou divisao inteira
5 % 2 == 1  # Resto da divisao
5**2 == 25  # Potenciacao
# Dois sinais de igual idicam realmente que os dois lados são iguais. Muito usado em lógica!
# Um sinal de igual é para armazenar variaveis

# A ordem de execucao de um calculo seguira:
#   (), potenciacao, mutiplicacao ou divisao ou resto ou modulo, subtracao ou adicao

# Pode-se fazer operacoes com str
print('oi'*3)  # resultado sera oioioi

# FORMATACAO 

# Para alinhar ou prrencher espacos pode-se usar {:}
a1 = input('Qual seu nome? ')
print('Seja bem vindo {:20}'.format(a1))  # escreve a variavel em 20 espacos
print('Seja bem vindo {:>20}'.format(a1))  # escreve a variavel em 20 espacos alinhado a esquerda
print('Seja bem vindo {:<20}'.format(a1))  # escreve a variavel em 20 espacos alinhado a direita
print('Seja bem vindo {:^20}'.format(a1))  # escreve a variavel em 20 espacos centralizado
print('Seja bem vindo {:=20}'.format(a1))  # escreve a variavel em 20 espacos com o sinal preenchendo

# para ajustar casas decimais pode-se usar {:.3f} le-se 3 casas decimais apos o ponto flutuante
soma = 1 + 1
print('A soma e de 1 mais 1 é {:.5f}' .format(soma))  # 5 casas decimais

# pra quebrar a linha usa-se \n
print('linha 1 \nlinha2')
# para nao quebrar a linha end=''
print('linha1', end='')
print('linha2')

# IMPORTAR MÓDULOS

# adciona funcionalidades, bibliotecas
#   biblioteca math -> ceil, floor, trunc, pow, sqrt, factorial
import statistics  # para importar todas as 'ferramentas' contidas na biblioteca estaticica
from statistics import mean  # economiza memoria. importa apenas a media da biblioteca estatistica

# para encontrar mais bibliotecas padrões:
#   python.org > documentation > library references

# para encontrar bibliotecas da comunidade
#   python.org > pypi > procurar biblioteca > verificar cheat sheet da biblioteca 
#   ou procurar e settings > project interpreter NO PYCHARM

# EXEMPLOS:
print('Olá usuário! Seja bem vindo!')
nome = str(input('Por favor, informe seu nome: '))  # usuario definira um texto
idade = int(input('Sua idade: '))  # usuario definira um inteiro
sexo = str(input('Seu sexo: '))  # usuario definira um texto
altura = float(input('Digite sua altura em metros: '))  # usuario definira um ponto flutuante
peso = float(input('Digite seu peso em kilos: '))  # usuaria definira um ponto flutuante
calc = altura * peso / 5  # calculo qualquer
print('{}, com {} anos, sendo do sexo {}, seu imc é de {}' .format(nome, idade, sexo, calc))
# dentro das mascaras serao adiciodas as variaveis colocadas na funcao .format()

import math  # importa todas as ferramentas contidas em math. ler a biblioteca em python.org
num = int(input('Digite um número: '))
raiz = math.sqrt(num)  # quando importa a biblioteca toda usa-se nomebiblioteca.ferramenta()
print('A raiz quadrada de {} é igual a {:.2f}.' .format(num, raiz))
print('E elevado a {} o resultado é {}' .format(2.5, math.ceil(num**num)))

# para economizar memória pode-se usar :

from math import sqrt, floor  # importado apenas duas ferramentas da biblioteca matematica
num2 = float(input('digite um número: '))
raiz2 = sqrt(num)  # dessa forma não precisa digitar a bibliteca. antes da ferramenta
print('A raiz de {} é igual a {}' .format(num2, floor(raiz2)))

import emoji  # biblioteca baixada, nao é biblioteca padrao do python
print(emoji.emojize('Python is :snowman:'))
