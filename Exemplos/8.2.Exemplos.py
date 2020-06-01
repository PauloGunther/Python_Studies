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
