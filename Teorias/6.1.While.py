
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


    