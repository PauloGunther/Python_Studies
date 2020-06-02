#DETERMINANDO POSIÇÕES

l = []
for c in range(0,5):
    l.append(int(input(f'Digite um valor para a posição {c}: ')))
print('='*50)
print(f'Voce digitou os valores: {l}')

maior = max(l)
print(f'O maior valor digitado foi {maior} nas posições: ', end = '')
for x, y in enumerate(l):
    if y == maior:
        print(f'{x} ', end = '')
print('')

menor = min(l)
print(f'O maior valor digitado foi {menor} nas posições: ', end = '')
for x, y in enumerate(l):
    if y == menor:
         print(f'{x} ', end = '')
print('')    
print('='*50)
print('')

#ADICIONAR APENAS VALORES INEDITOS NUMA LISTA

l2 = list()

while True:
    l2.append(int(input('Digite um valor: ')))
    if l2.count(l2[-1]) > 1:
        l2.pop()
        print('Não vou adicionar. Valor Duplicado!')
    decisao = str(input('Deseja continuar? [N/S]: ')) .upper().strip()
    if decisao in 'N':
        break
l2.sort()
print(f'Você digitou {l2}')

print('')    
print('='*50)
print('')

#ADICIONAR VALORES NA LISTA EM POSICOES CORRETAS

l3 = []
for cont in range(0, 5):
    a3 = int(input('Digite um numero: '))
    if cont == 0 or a3 > l3[-1]:
        l3.append(a3)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(l3):
            if l3[pos] >= a3:
                l3.insert(pos, a3)
                break
            pos += 1
            
print(l3)
print('')    
print('='*50)
print('')


#ANALISAR LISTA CRIADA
            
l4 = []
while True:
    l4.append(int(input('Digite um numero: ')))
    decisao = str(input('Deseja adicionar mais um numero [S/N]: ')) .upper().strip()
    if decisao == 'N':
        break
print(f'Foram digitados {len(l4)} numeros.')
l4.sort(reverse=True)
print(f'A lista ordenada de forma decrescente: {l4}')
if 5 in l4:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 nao esta na lista.')
  
print('')    
print('='*50)
print('')

#LISTA PAR E IMPAR
l5 = []
while True:
    l5.append(int(input('Digite um numero: ')))
    decisao = str(input('Deseja adicionar mais um numero [S/N]: ')) .upper().strip()
    if decisao == 'N':
        break
lpar = []
limpar = []
for contador in l5:
    if contador % 2 == 0:
        lpar.append(contador)
    else:
        limpar.append(contador)

print(f'A lista padrao: {l5}')
print(f'A lista par: {lpar}')
print(f'A lista impar: {limpar}')

print('')    
print('='*50)
print('')

#VERIFICAR SE O NUMERO DE PARENTES QUE FECHA E O MESMO QUE ABRE

a1 = str(input('Digite uma exprecao: '))
print(a1[2])

if a1.count('(') == a1.count(')'):
    print('Expressao valida')
else:
    print('Expressao invalida')


