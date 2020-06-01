#ESCREVER NUMERO POR EXTENSO

a = int(input('Digite um numero entre 0 e 10: '))
while a > 20 or a < 0:
    a = int(input('Tente novamente. Digite um numero entre 0 e 10: '))

ext = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
print(f'Voce digitou o numero {ext[a]}')

#TABELA BRASILEIRAO 2019

bras = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print(f'Lista dos 5 primeiros colocados:\n{bras[0:5]}')
print(f'Lista dos 5 ultimos colocados:\n{bras[-4:]}')
print(f'A lista por ordem alfabetica:\n{sorted(bras)}')
chap = bras.index('Chapecoense')
print(f'A chapeconense esta na {chap+1} posicao')

#SORTEANDO NUMERO ALEATORIOS E COLOCAND EM TUPLA

from random import randint


y3 = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('O valores sorteados sao: ', end = '')
for c3 in y3:
    print(f' {c3}', end = '')
print(f'\nO maior numero e: {max(y3)}')
print(f'O menor numero e: {min(y3)}')

#encontradno tuplas

a4 = int(input('Digite um numero:'))
b4 = int(input('Digite outro numero:'))
c4 = int(input('Digite mais um numero:'))
d4 = int(input('Digite o ultimo numero:'))

y4 = (a4, b4, c4, d4)
print(f'voce digitou os valores: {y4}')
if y4.count(9) > 0:
    print(f'o valor 9 aparece {y4.count(9)} vezes')
else:
    print(f'o valor 9 aparece nao aparece nenhuma vez')

if 3 not in y4:
    print('O valor 3 nao foi digitado.')
else:
    print(f'o valor 3 esta na posicao {y4.index(3)+1}')
print('Os valores pares digitados: ', end = '')
for x4 in y4:
    if x4 % 2 ==0:
        print(f'{x4} ', end = '')
print('')

#LISTA DE PRECOS

lp = (  'Pao', 1.5, 
        'Torresmo', 14.90, 
        'Leite', 2.9, 
        'Pimentao', 5.4)

print('-'*40)
print('{:^40}' .format('LISTA DE PRECO'))
print('-'*40)
for c5 in range(0, len(lp), 2):
    print('{:.<30} R$ {:>6.2f}' .format(lp[c5], lp[c5+1]))


#LISTA VOGAIS

y5 = ('carro', 'torresmo', 'cerveja', 'traficante')

for c5 in y5:
    print(f'Na palavra {c5} temos:', end ='')
    for c6 in c5:
        if c6.lower().strip() in 'aeiou':
            print(f' {c6}', end = '')
    print('')

