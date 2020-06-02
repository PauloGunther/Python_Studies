#FOGOS DE ARTIFICIO

from time import sleep
import emoji
print('Contagem regressiva em:')

for c in range(5, 0, -1):
    print(c, 'segundos')
    sleep(1)
print(emoji.emojize('BOOOOM!:tada:', use_aliases=True))

#TODOS OS NÚMEROS PARES
for c in range(1, 51):
    if c % 2 == 0:
        print(c)

#SOMA DOS MULTIPLOS DE 3
s = 0
for c in range(1, 500):
    if c % 2 != 0 and c % 3 == 0:
        s = c + s
print(s)

#TABUADA
x = int(input('Digite um número: '))
print('A tabuada desse número é: ')
for c in range(0, 11):
    print('{} x {} = {}' .format(x, c, c*x))

#A SOMA DE 6 NÚMERO PARES INTEIROS
s = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = n + s
print(s)

#MOSTRAR OS 10 PRIMEIROS TERMOS DE UMA PA
a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razao da PA: '))
for c in range(0,10):
    pa = a1 + r*c
    print(pa)

#VERIFICAR SE É PALINDROMO
a = str(input('Digite uma frase: ')) .upper().replace(' ', '')
i = ''
for c in range(len(a)-1, -1, -1):
    i = i + a[c]
if i == a:
    print('Palindromo')
else:
    print('Nao e palindromo')

#VERIFICAR SE É PRIMO
a = int(input('Digite um número: '))
i = 0
for c in range(1, a+1):
    b = a % c == 0
    i = b + i
if i > 2:
    print('{} não é primo!' .format(a))
else:
    print('{} é primo!' .format(a))

#QUANTAS PESSOAS ATINGIRAM A MAIORIDADE?
from datetime import date
sm = 1
sM = 1
for c in range(0, 7):
    a = int(input('Digite o ano de nasceimnto: '))
    if date.today().year - a >= 21:
        sm = sm + c
    else:
        sM = sM + c
print('{} pessoas maior de idade\n{} pessoas menor de idade.' .format(sm, sM))

#MAIOR PESO
l = []
for c in range(0, 5):
    p = l.append(float(input('Digite o peso em kg: ')))
print('O maior peso é {} kg e o menor é {} kg' .format(max(l), min(l)))
menor = 0
maior = 0
for c in range(0, 6):
    peso = float(input('Digite o peso: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

# ANALISADOR COMPLETO
np = 4
totidade = 0
mi = 0
nhv = 0
tm20 = 0
for c in range(0, np):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    totidade += idade
    sexo = str(input('Digite o sexo: '))

    if c == 0 and sexo in 'Mm':
        mi = idade
        nhv = nome
    elif idade > mi and sexo in 'Mm':
        mi = idade
        nhv = nome

    if idade < 20 and sexo in 'Ff':
        tm20 += 1

print('A média de idade do grupo é: {}' .format(totidade/np))
print('O homem mais velho do grupo é {} com {} anos' .format(nhv, mi))
print('O número de melheres com menos de 20 anos é {}' .format(tm20))

#MEDIA DE IDADE

np = 4
totidade = 0
mi = 0
nhv = 0
tm20 = 0
for c in range(0, np):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    totidade += idade
    sexo = str(input('Digite o sexo: '))

    if c == 0 and sexo in 'Mm':
        mi = idade
        nhv = nome
    elif idade > mi and sexo in 'Mm':
        mi = idade
        nhv = nome

    if idade < 20 and sexo in 'Ff':
        tm20 += 1

print('A média de idade do grupo é: {}' .format(totidade/np))
print('O homem mais velho do grupo é {} com {} anos' .format(nhv, mi))
print('O número de melheres com menos de 20 anos é {}' .format(tm20))
