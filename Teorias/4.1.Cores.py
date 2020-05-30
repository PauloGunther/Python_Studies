#CORES
#\033[0;33;44m
#padrão ANSI
# [style;text;back
# style:    0 > none
#           1 > bold
#           4 > underline
#           7 > negative

#text:  30, 31, 32, 33, 34, 35, 36, 37 > cores letras
#BRANCO, VERMELHO, VERDE, AMARELO, AZUL, ROXO, AZUL, CINZA
#back: 40, 41, 42, 43, 44, 45, 46, 47 > cores de fundo

print('\033[1;31;43mOlá, Mundo!')
print('\033[0;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[7;40mOlá, Mundo!\033[m')

a = 1
b = 2
print('Os números são \033[1;31m{}\033[m e \033[1;33;46m{}\033[m.' .format(a, b))

nome = 'Paulo Augusto'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'preto':'\033[7;30m'}
print('Bem vindo {}{}{}!' .format(cores['preto'], nome, cores['limpa']))
