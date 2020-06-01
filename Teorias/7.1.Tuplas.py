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
