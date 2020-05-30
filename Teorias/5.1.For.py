
#ação irá acotecer o número e da forma que os parâmetros do range determinarem
#função usada para repetir ação

for c in range(0, 5): #contar de 0 - 4 - a variavel c funciona como um contador
    print(c) # Irá printar 5 vezes pois está dentro do for
print('Fim')

for d in range(3, 0, -1): #contar de trás para frente usa-se o 3º elemento negativo
    print(d) 
for e in range(0, 7, 2): #pulando dois números
    print(e)

i = int(input('Inicio: '))
f = int(input('Final: '))
p = int(input('Passo: '))
for a in range(i, f+1, p): # irá printar conforme as variaeis forem definidas
    print(a)

s = 0 # para criar um somatorio
for b in range(0, 4):
    n = int(input('Digite um número: ')) #para definiar 4 variaveis
    s = s + n # pode ser escrito como s += n -> usa-se como soma doas valores definidos
print('A soma é: {}' . format(s))

for c in range(0, 3):
    print('Oi') #pode-se usar string, irá printar 5 vezes
print('fim')
