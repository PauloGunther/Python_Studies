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
    u3 = str(input('Par ou Impar? [P/I]: ')) .upper().strip()[0]
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

#CADASTRAR PESSSOAS
b4 = c4 = ''
tot184 = toth4 = totm4 = 0
while True:
    print('-'*30)
    a4 = int(input('Idade: '))
    while b4 not in 'MF':
        b4 = str(input('Sexo [M/F]: ')) .strip().upper()
    print('-'*30)
    
    if a4 > 18:
        tot184 += 1
    if b4 == 'M':
        toth4 += 1
    if a4 < 20 and b4 == 'F':
        totm4 += 1 

    while c4 not in 'SN':
        c4 = str(input('Deseja continuar? [S/N]: ')) .strip().upper()
    if c4 == 'N':
        break
    else:
        b4 = c4 = ''

print('-'*30)    
print(f'O total de pessoas com mais de 18 anos é {tot184}.')
print(f'Ao todo temos {toth4} homens cadastrados.')
print(f'E temos {totm4} mulher com menos de 20 anos.')


#CADASTRO DE PRODUTOS 
print('-'*30)
print('{:^30}' .format('LOJA SUPER BARATAO'))
print('-'*30)
s5 = totmaior5 = tot5 = menor5 = 0
c5 = nome5 = ''
while True:
    a5 = str(input('Nome do produto: '))
    b5 = float(input('Preço R$: '))
    s5 += b5
    
    if b5 > 1000:
        totmaior5 += 1
    
    tot5 += 1
    if tot5 == 1:
        menor5 = b5
        nome5 = a5
    if b5 < menor5:
        menor5 = b5
        nome5 = b5
        
    while c5 != 'S' and c5 != 'N':
        c5 = str(input('Quer continuar? [S/N]: ')) .upper().strip()
    if c5 == 'N':
        break
    c5 = ''
print(f'O total da compra foi de {s5:.2f}')
print(f'Temos {totmaior5} custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nome5} que custo R${menor5:.2f}')

#CAIXA ELETRONICO
print('-'*30)
print('{:^30}' .format('CAIXA ELETRONICO'))
print('-'*30)

a6 = int(input('Quanto você deseja sacar? R$ '))

tot50 = tot20 = tot10 = tot1 = 0
while a6 - 50 > 0:
        a6 = a6 - 50
        tot50 += 1
while a6 - 20 > 0:
        a6 = a6 - 20
        tot20 += 1
while a6 - 10 > 0:
        a6 = a6 - 10
        tot10 += 1   
while a6 - 1 > -1:
        a6 = a6 - 1
        tot1 += 1 
print(f'Total de {tot50} cédulas de R$50,00')
print(f'Total de {tot20} cédulas de R$20,00')
print(f'Total de {tot10} cédulas de R$10,00')
print(f'Total de {tot1} cédulas de R$1,00')
print('-'*30)
print('{:^30}' .format('VOLTE SEMPRE')) 
