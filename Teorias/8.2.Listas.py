#LISTAS COMPOSTAS
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
    