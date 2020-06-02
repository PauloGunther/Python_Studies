#=======IF=======

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))

from statistics import mean #média importada
m = mean([n1, n2, n3])
print('Sua média é: {:.2f}' .format(m))

if m >= 7: # se a média for maior que 7. Nao esquecer dois ponto :
    print('Congrats, aprovado!') #precisa ser escrito com tab, pois esta subordinado ao IF
else: # se não for maior que 7
    print('Burro pra caralho!') #precisa ser escrito com tab, pois esta subordinado ao ELSE

nome = str(input('Qual o seu nome? '))
if nome == 'Paulo': #se o nome foi igual a paulo
    print('Que nome bonito!') #CONDIÇÃO SIMPLES não precisa do else (se não)
print('Tenha um bom dia, {}.' .format(nome)) #condição que sempre vai ocorrer pois esta fora do if

nome = str(input('Qual o seu nome? '))
if nome == 'Paulo': #se
    print('Que nome bonito!')
else: #se nao. Se o nome nao foi igual a paulo
    print('Seu nome é bem normal') #ESTRUTURA CONDICIONAL COMPOSTA
print('Tenha um bom dia, {}.' .format(nome)) #como esta fora do tab irá ocorrer de qualquer maneira

nome = str(input('Qual o seu nome? '))
if nome == 'Paulo':
    print('Que nome bonito!')
elif nome =='Pedro' or nome== 'Ana': #funciona como outra condição se, que nao esta subordinada a primeira
    print('Seu nome é popular no Brasil!.')
elif nome in ('Ana Cláudia Jéssica Ellen'): #leia-se 'e se'
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal') #ESTRUTURA CONDICIONAL ANINHADA - ha varias condições/ramificações
print('Tenha um bom dia, {}.' .format(nome))

#=======FOR======
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

#=======WHILE
#FUNCIONA COMO FOR(USADO PARA REPETIR), MAS EM VEZ DE SER DETERMINADA PELO RANGE É DETERMINADA POR UMA CONDIÇÃO
while True: # condição se repetirá para sempre e nunca tera fim
    print ('Para sempre')

n = 0
while n != 999: # condição irá se repedir até digitar 999
    n = int(input('Digite um número: '))

n = contador = 0
while contador == 5: # condição irá se repetir até contador for 5
    n = int(input('Digite um número: '))
    contador += 1

#PODE-SE USAR BREAK PARA SAIR DE UM WHILE
contador = 0
while True: # irá repetir para sempre
    n = int(input('Digite um número: '))
    contador += 1
    if contador == 5: #mas se o contador atingir 5
        break # Saíra do while (repetição)


    
