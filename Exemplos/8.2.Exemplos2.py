#LISTA DE PESSOAS E PESOS

l1 = []
pessoas = []
maior = menor = 0
nomemaior = []
nomemenor = []
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    l1.append(pessoas[:])
    pessoas.clear()
    
    for c in l1:
        if maior == 0:
            maior = c[1]
            nomemaior = c[0]
            menor = c[1]
            nomemenor = c[0]
        elif c[1] >= maior:
            maior = c[1]
            nomemaior += c[0]
        elif c[1] <= menor:
            menor = c[1]
            nomemenor += (c[0])


    deci = str(input('Deseja continuar? [S/N]: ')) .upper().strip()
    if deci == 'N':
        break


    
print(f'Ao todo você cadastrou {len(l1)} pessoas.')
print(f'O maior peso foi {maior} kg. Peso de {nomemaior}')
print(f'O menor peso foi {menor} kg. Peso de {nomemenor}')

#SEMPRAR VALORES EM PARES E IMPARES

l = list()
pares = []
impares = []
l.append(pares)
l.append(impares)

for c in range(0, 7):
    a1 = int(input('Digite um valor: '))
    if a1 % 2 == 0:
        pares.append(a1)
        pares.sort()
    else:
        impares.append(a1)
        impares.sort()


print(f'O números pares sao : {l[0]}')
print(f'O números impares sao : {l[1]}')
