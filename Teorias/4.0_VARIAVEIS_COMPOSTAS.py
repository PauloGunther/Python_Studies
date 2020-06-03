#======TUPLAS=======

#MAIS DE UMA VARIAVEL DEFINIDA NO MESMO "ESPAÇO". USAR ()

lanches = ('Hamburguer', 'Batata Frita', 'Pizza', 'Pudim') #isso é uma tupla

print(lanches) #printa todos os elemetos da tupla
print(lanches[0]) #printa o primeiro elemento da tupla
print(lanches[1:]) #printa todos os elementos a partir do segundo
print(lanches[0:3]) #printa até o 3 elemento
print(lanches[-1]) #ultimo elemento

#lanches[3] = 'Suco' #erro pois tuplas são imutáveis. Não pode adicionar ou subtituir variaveis nas tuplas

for contador in range (0, len(lanches)):
    print(f'Vou comer {lanches[contador]}') #imprime lanche por lanche - melhor quando precisa saber posição

for comida in lanches:
    print(f'Vou comer {comida}') #imprime lanche por lanche como exemplo de cima

for contador in range (0, len(lanches)):
    print(f'Vou comer {lanches[contador]} na posição {contador}') #saber posição

for posicao, comida in enumerate(lanches): #enumerate caso precise saber posição
    print(f'Vou comer {comida} na posição {posicao}') 

print(sorted(lanches)) #irá printar lanches em ordem alfabética. Apeas printar. (transformou a tupla em lista [])
print(lanches) #mas o sorted não altera o tupla. Ela continua imutavel.

a = (1, 2, 5)
b = (3, 4, 6, 2)
c = a + b #junta os elementos das duas tuplas formando uma tupla de 6 elementos
d = b + a # a ordem da soma para tuplas importa
print(c) 
print(d)

print(c.count(2)) #contar quantos 2 tem na tupla
print(c.index(2)) # mostra a poisção que aparece o primeiro 2
print(c.index(2,2)) #mostra a posição a partir da posição 2

#========LISTAS==========

#MAIS DE UMA VARIAVEL DEFINIDA NO MESMO "ESPAÇO". USAR []
#DIFERENTE DAS TUPLAS, LISTAS SÃO MUTAVEIS - PODE-SE FAZER OPERAÇÕES DE ADIÇÃO OU REMOÇÃO DE ELEMENTOS

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

#========LISTAS COMPOSTAS========

#Lista dentro de listas

teste = list()
teste.append('Paulo')
teste.append(27)
gurizada = list()
gurizada.append(teste[:]) #colocado uma copia da lista em gurizada, pois foi usado [:]
print(gurizada)
teste[0] = 'Ellen' #adicionado a lista teste inicial
teste[1] = 24 #adicionado a lista teste inicial
gurizada.append(teste) #lista teste inicial adicionada da gurizada
print(gurizada)

gurizada = [['Pedro', 20], ['Joao', 19], ['Maria', 21]] #3 listas dentro de uma lista

print(gurizada[2][1]) #primeiro termo e referente a posicao na lista "mae"
print(gurizada[1][0]) #segundo termo e posicao dentre da sublista

for p in gurizada:
    print(p) #printa todas sublistas dentro de gurizada

for p in gurizada:
    print(p[0]) # printa somente o nome dentro das sbulistas
for p in gurizada:
    print(p[1]) # printa somente a idade dentro das sublistas 

principal = []
dados = []

for c in range(0,3):
    dados.append(str(input('Nome: '))) #add informacadao em dados
    dados.append(int(input('Idade: '))) #add informacadao em dados
    principal.append(dados[:]) #add dados em principal [:] -> copia de dados
    dados.clear() # se nao limpar a informacao anterior vai ser add dentro na nova lista

print(principal)
for p in principal:
    print(f'Printa o nome {p[0]}. Printa a idade {p[1]}')

#======DICIONARIOS=======

#assim como tuplas e listas sao variaveis compostas
#agora definidas {}
#serve paa atribuir 'nomes' a espaços nas listas

pessoas = {'nome': 'Paulo', 'sexo': 'M', 'idade': 22} #declarando um dicionario
#nome é uma chave, paulo é um valor. o conjunto de chaves compoe um item (value>keys>items)

print(pessoas) #ira mostrar o item exatamente como adicionado acima
print(pessoas['nome']) #ira mostrar o valor atribuido a chave nome
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #quando usar o format, precisa usar aspas duplas " pois esta dentro das aspas simples

print(pessoas.items()) #mostra o conjuto completo separando keys em tuplas
print(pessoas.keys()) #mostra apenas as keys
print(pessoas.values()) #mostra os valores nas keys

for c in pessoas:
    print(c) #mostra as keys
for c in pessoas.keys():
    print(c) #também mostra as keys

for c in pessoas.values():
    print(c) #mostra os valores
for k, v in pessoas.items():
    print(k, v) #k sera as keys e v os valores. nao precisa de enumarate como nas litas e tuplas

pessoas['nome'] = 'Gustavo' #substitui o valor anterior em nome. nao precisa dar append

estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil = []

brasil.append(estado1) #posso adicionar um dicionario dentro de uma lista
brasil.append(estado2)
print(brasil) #mostra os dicionarios dentro da lista
print(brasil[1]) #mostra o dicionario na posição 1
print(brasil[1]['sigla']) #mostra o valor da chave sigle no dicionário 1

#EXEMPLO
estado = dict() #criado um diconário
brasil = list() #criado um lista

for c in range(0,3):
   estado['uf'] = str(input('Unidade federativa: '))
   estado['sigla'] = str(input('Sigla: '))
   brasil.append(estado.copy()) #nao pode usar [:] para criar uma copia de biblioteca. por isso usar .copy()
for e in brasil:#vai percorrer as bibliotecas de brasil
    print(e) #mostra biblioteca por biblioteca

for e in brasil: 
    for k, v in e.items(): #onde k vai ser chaves e v os valores
        print(f'O chave {k} tem valor {v}') #mostra valores e suas rescpecticas chaves

for e in brasil:
    for v in e.values():
        print(v) # mostra todos os valores de todas as chaves