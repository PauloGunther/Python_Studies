
#LISTA DE PESSOAS E PESOS
l1 = []
pessoas = []
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    if maior == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] >= maior:
            maior = pessoas[1]
        elif pessoas[1] <= menor:
            menor = pessoas[1]
    
    l1.append(pessoas[:])
    pessoas.clear()
    deci = str(input('Deseja continuar? [S/N]: ')) .upper().strip()
    if deci == 'N':
        break
    
print(f'Ao todo você cadastrou {len(l1)} pessoas.')
print(f'O maior peso foi {maior} kg. Peso de: ')
for c in l1:
    if c[1] == maior:
        print(c[0])
print(f'O menor peso foi {menor} kg. Peso de: ')
for c in l1:
    if c[1] == menor:
        print(c[0])
print()    
print('='*50)
print()

#SEPARAR VALORES EM PARES E IMPARES
l = [[], []]
for c in range(0, 7):
    a1 = int(input(f'Digite o {c} valor: '))
    if a1 % 2 == 0:
        l[0].append(a1)   
    else:
        l[1].append(a1)
        l[1].sort()

l[1].sort()
l[0].sort()
print(f'O números pares sao : {l[0]}')
print(f'O números impares sao : {l[1]}')
print()    
print('='*50)
print()

#CRIAR UMA MATRIZ NA TELA 3X3
m = []
l = []
for c in range (0,3):
    for d in range (0,3):
        l.append(int(input(f'Digite um numero para [{c}, {d}]: ')))
    m.append(l[:])
    l.clear()

for c in m:
    for d in range(0,3):
        print(f'[ { c[d]} ]', end ='')
    print()

#MANIPULAR NUMEROS DA MATRIZ
s = s3 = maior =0
for c in m:
    for d in range(0, 3):
        s = c[d] + s       
    s3 = s3 + c[2]  
for c in m[1]:
    if c == 0:
        maior = c
    elif c > maior:
        maior = c
   
print(f'A soma dos valores: {s}\nA soma da 3ª coluna: {s3}\nO maior numero da segunda linha: {maior}')
print()    
print('='*50)
print()

#GERAR NUMEROS DA MEGASENA
from random import randint
from time import sleep

a1 =  int(input('Quantos jogos quer gerar? '))
print(f'Sorteando {a1} jogos...')
for c in range(0, a1):
    l = []
    for d in range(0, 6):
        num = randint(0,60)
        while num in l:
            num = randint(0,60)
        l.append(num)
    l.sort()        
    print(f'Jogo {c+1}: {l}')
    sleep(1)
print()    
print('='*50)
print()

#GERAR BOLETIM
l = []
alunos = []
notas = []
while True:
    alunos.append(str(input('Nome: ')))
    notas.append(int(input('Nota 1: ')))
    notas.append(int(input('Nota 2: ')))
    alunos.append(notas[:])
    l.append(alunos[:])
    alunos.clear()
    notas.clear()

    dec = str(input('Deseja continuar? [S/N]: ')) .upper().strip()
    if dec in 'N':
        break
cont = 0
print('='*40)
print(f'{"nº":<4} {"NOME":<20} {"MEDIA"}')
for c in l:
    s = 0
    for d in range(0, 2):
        s = c[1][d] + s
    print(f'{cont:<4} {c[0]:<20} {s/2}')
    cont += 1
print('='*40)

while True:
    a = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    if a == 999:
        break
    print(f'As notas de {l[a][0]} são: {l[a][1]}')
    print('='*40)
print('VOLTE SEMPRE!')
