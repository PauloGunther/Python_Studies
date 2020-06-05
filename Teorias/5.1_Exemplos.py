from time import sleep
from random import randint


# AREA DO TERRENO
def area(x, y):
    a = x * y
    print(f'A area de um terreno {x}x{y} é de {a:.2f}m².')


a = float(input('Comprimento: '))
b = float(input('Largura: '))
area(a, b)


# FORMACATAO ACOMAPNHA TEXTO
def form(texto):  # funcao
    tamanho = len(texto)
    print('-'*(tamanho+5))
    print(f'  {texto}')  # Dois espaços antes de inicia centraliza a mensagem
    print('-'*(tamanho+5))


form('MATRIX')
form('SE O TEXTO FOR MAIOR?')


# CONTAGENS
def lin():
    print('-'*40)


def contagem(a, b, c):
    if a > b:
        for i in range(a, b-1, -c):
            print(f'{i} ', end='')
            sleep(0.5)
    else:
        for i in range(a, b+1, c):
            print(f'{i} ', end='')
            sleep(0.5)
    print('Fim!')
    lin()


contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora é sua vez: ')
contagem(a=int(input('Inicio: ')),
         b=int(input('Fim: ')),
         c=abs(int(input('Passo: '))))
lin()
lin()


# FUNCAO MAIOR
def maior(*n):
    print('Analisando os valores...')
    cont = maior = 0
    for i in n:
        if cont == 0:
            maior = i
        elif i > maior:
            maior = i
        cont += 1
        print(f'{i} ', end='')
    print(f'Foram {cont} valores ao todo.')
    print(f'O maior valor foi {maior}.')
    lin()


maior(1, 2, 8, 21, 9)
maior(1, 8, 6, 1, 99)
maior(95, 20, 10, 55)
lin()


# SORTEIO E SOMA DE PARES
def sorteio(sor):
    for i in range(0, 5):
        a = randint(0, 10)
        print(f'{a} ', end='')
        sor.append(a)
    print('Pronto!')


def somapar(sor):
    s = 0
    for i in sor:
        if i % 2 == 0:
            s += i
    print(f'A soma dos valores {sor} é {s}')


lst = []
sorteio(lst)
somapar(lst)
