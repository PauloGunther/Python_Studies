
#FUNCIONA COMO FOR(USADO PARA REPETIR), MAS EM VEZ DE SER DETERMINADA PELO RANGE É DETERMINADA POR UMA CONDIÇÃO

s = 'X'
while s != 'M' and s != 'F': #lógica abaixo irá continuar a ser executado enquanto a condição não for atendida
    s = str(input('Digite seu sexo [M/F]: ')) .upper().strip()
    if s != 'M' and s != 'F':
        print('Por favor digite novamente!')