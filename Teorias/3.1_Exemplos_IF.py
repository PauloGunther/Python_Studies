# ADIVINAHNDO O QUE O COMPUTADO ESTA PENSANDO
from random import choice
from time import sleep
x = choice('0 1 2 3 4 5' .split()) #PODERIA TER USADO RANGINT DO RANDOM
n = int(input('Advinhe o número que estou pensando de 0 a 5: '))
print('Processando...')
sleep(2) #AGUARDAR UM TEMPO
if n == int(x):
    print('Você acertou!')
else:
    print('Tente novamente, o valor era {}'.format(x))

#CALCULANDO MULTA
vel = int(choice('50 55 60 65 70 75 80 85 90 95 100' .split()))
print('Sua velocidade é foi de {} km/h.' .format(vel))
if vel >=80:
    print('Você foi multado em R$ {:.2f}.' .format(7*(vel-80)))
print('Você não foi multado!') #CONDIÇÃO SIMPLIFICADA NÃO PRECISA DO ELSE

#SE É PAR OU IMPAR
n1 = int(input('Digite um número inteiro: '))
if n1 % 2 == 0:
    print('O número é par!')
else:
    print('O número é impar.')

#ANO BISSESTO
from datetime import date
ano = int(input('Digite um ano: Coloque 0 para analisar o ano atual.'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano bissesto!')
else:
    print('Ano não é bissesto!')

#ENCONTRANDO O MAIOR E MENOR
a1 = int(input('Digite um número: '))
a2 = int(input('Digite outro número: '))
a3 = int(input('Digite mais um número: '))
x = list([a1, a2, a3])
print('O maior valor é: {}' .format(max(x)))
print('O menor valor é: {}' .format(min(x)))

#SE AS RETAS POODEM FORMAR UM TRIANGULO
x1 = int(input('Digite um número: '))
x2 = int(input('Digite outro número: '))
x3 = int(input('Digite mais um número: '))
if abs(x1-x2) < x3 < x1+x2 and abs(x1-x3) < x2 < x1+x3 and abs(x3-x2) < x1 < x3+x2:
    print('O trinagulo existe!')
else:
    print('O triangulo não existe.')
