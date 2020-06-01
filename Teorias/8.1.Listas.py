#VARIAVEL COMPOSTA
# MAIS DE UMA VARIAVEL DEFINIDA NO MESMO "ESPAÇO". USAR []
# DIFERENTE DAS TUPLAS, LISTAS SÃO MUTAVEIS - PODE-SE FAZER OPERAÇÕES DE ADIÇÃO OU REMOÇÃO DE ELEMENTOS

lista = [2, 5, 8, 3]
lista[2] = 7 #troca o numero 8 pelo 7
print(lista)

lista.append(8) #adiciona um elemento na lista, ele será colocada no últioma posição
print(lista)

lista.insert(2, 0) #adiciona um alemento numa posição especifica, no exemplo na posição 2
print(lista)

lista.sort() #organiza de forma crescente a lista
lista.sort(reverse=True) #organiza de forma decrescente

print(f'O tamanho da lista é de {len(lista)} variaveis') #tamanho da lista

lista.pop() #elimina o ultiom elemento da lista
lista.pop(2) #elimina a posição da lista

lista.remove(2) #remove o elemento 2 da lista, se houverem mais que um elemento 2, ele remove o primeiro

valores = [] #cria uma lista vazia
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores: #ira mostrar os valores dentro da lista
    print(f'Os valores são: {v} ', end = '')
print('')
print('')
for c, x in enumerate(valores): #ira mostrar a posição e o valor da lista
    print(f'Na posicação {c} tem o valor {x}.')

lista2 = [] #ou valores = list()

for cont in range(0,3): #adicionar valores a uma lista
    lista2.append(int(input('Digite um valor: ')))
print(lista2)

a = [2, 3, 8]
b = a #cria uma ligação entre as listas
b[2] = 7 # de modo que se alterar a lista B a lista A tambem altera
print(f'Lista A: {a}')
print(f'Lista B: {b}') #listas continuam iguais pois estao ligadas

a = [2, 3, 8]
b = a[:] #faz um copia da lista a
b[2] = 7 # de modo que se alterar a lista B a lista A NAO se altera
print(f'Lista A: {a}')
print(f'Lista B: {b}') #agora as listras estao diferentes

