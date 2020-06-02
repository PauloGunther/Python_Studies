#DIGITAR SOMENTE O QUE ESTA SENDO PEDIDO
s = ''
while s != 'M' and s != 'F':
    s = str(input('Digite seu sexo [M/F]: ')) .upper().strip()
    if s != 'M' and s != 'F':
        print('Por favor digite novamente!')
print('Sexo computado!')

#MELHORANDO ADIVINHAÇÃO
from random import randint
from time import sleep
print('Pensarei em um número entre 0 e 10. Tente adivinhar.')
y = randint(0, 10)
print('Pensando...')
sleep(4)
x = -1
c = 1
while x != y:
    x = int(input('Digite um número: '))
    if x > 10 or x < 0:
        print('Número Inválido.Tente novamente')
    elif x != y:
        print('Você errou. Tente novamente.')
        c += 1
print('Você acertou, após {} tentativas!' .format(c))

#CALCULADORA COM OPÇOES PRO USUARIO
print('='*10, 'MENU', '='*10)
a = float(input('Digite um valor: '))
b = float(input('Digite um segundo valor: '))
o = 0
while o != 5:
    print('Por favor escolha a opção que preferir:')
    o = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos número\n[5] Sair do programa\n>>'))

    if o == 1:
        print('O resultado é: ', a + b)
    elif o == 2:
        print('O resultado é: ', a*b)
    elif o == 3:
        print('O resultado é: ', max(a,b))
    elif o == 4:
        a = float(input('Digite um valor: '))
        b = float(input('Digite um segundo valor: '))
        print('Por favor escolha a opção que preferir:')
        o = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos número\n[5] Sair do programa\n>>'))
    else:
        print('Número inválido, tente novamente!')
print('Até logo!')

#FATORIAL
a = int(input('Digite um valor: '))
f1 = 1
for c in range(1, a+1):
    f1 = c*f1
print('O fatorial é ', f1)
a = int(input('Digite um valor: '))
c = a
f = 1
while c > 0:
    f = f * c
    c -= 1
print(f)

#PA COM WHILE
a1 = float(input('Digite o primeiro termo: '))
r = float(input('Digite a razao da PA: '))
i = float(input('Digite o numero de termos das PA: '))
n = 0
while n != i:
    pa = a1 + r*n
    n =1+n
    print(pa)
a = str(input('Deseja mostrar mais termos? [S/N]: ')) .strip().upper()
if a == 'S':
    i = float(input('Digite o numero de termos a mais: '))
    n = 0
    while n != i:
        pa2 = pa + r * n
        n = 1 + n
        print(pa2)
else:
    print('Ate logo!')

#DIGITAR ATÉ 999
a=0
n=0
tot = 0
while a != 999:
    a = int(input('Digite um número: '))
    if a != 999:
        n += 1
        tot = a+tot
print(n,tot)

#MAIOR, SOMA E MENOR
x = 0
s = 0
c = 1
maior = 0
menor = 0
while x != 'N':
    a = int(input('Digite um valor: '))
    x = str(input('Deseja continuar digitando? [S/N]:  ')) .strip().upper()
    s += a
    if c == 1:
        menor = a
        maior = a
    else:
        if a > maior:
            maior = a
        elif a < menor:
            menor = a
    c += 1
print(s/c, maior, menor)

#FIBONACCI
t1 = 0
t2 = 1
x = int(input())
n = 2
while n < x:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    n = 1 + n
print(t3)
