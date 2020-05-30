#SOMA VALORES ATÉ A FLAG 999
s1 = 0 
c1 = 0
while True:
    a1 = int(input('digite um valor (999 para parar): '))
    if a1 == 999:
        break
    s1 += a1
    c1 += 1
print(s1, c1)


#MOSTRAR TABUADA ATE USUARIA DIGITAR NEGATIVO
while True:
    print('-' * 30)
    a2 = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if a2 < 0:
        break
    for c2 in range(1, 11):
        r2 = c2 * a2
        print(f'{a2} x {c2} = {r2}')
    
print('Tabuada encerrada!')


#JOGUE PAR OU IMPAR

print('-' * 40)
print('VAMOS JOGAR PAR OU IMPAR')
print('-' * 40)
from random import randint
c3 = 0
while True:
    x3 = randint(0, 10)
    u3 = str(input('Par ou Impar? [P/I]: ')) .upper().strip()
    a3 = int(input('Digite um valor: '))
    r3 = x3 + a3
    if r3 % 2 == 0:
        p3 = "P"
    else:
        p3 = "I"
    if p3 == u3:
        print(f'O computador jogo {x3} e você {a3}. O resultado é {r3}.\nVocê ganhou!\nVamos jogar novamente...')
        c3 += 1
    else:
        print(f'O computador jogo {x3} e você {a3}. O resultado é {r3}.\nVocê perdeu!')
        break
print(f'GAME OVER! Você venceu {c3} vezes.')
    

