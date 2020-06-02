#MANIPULANDO TEXTOS

#FATIAMENTO
frase = 'Curso em video python'
print(frase[9]) #retorna a letrade de pisção 9
print(frase[9:15]) #retorna as letras na posição 9 a 15
print(frase[2:15:2]) #retorna as letras na posição 2 a 15 pulando de 2 em 2
print(frase[:5]) #retorna as letras do inicio até a quinta
print(frase[5:]) #retorna as letras da quinta ao final
print(frase[5::2]) #retorna as letras da quinta ao final pulando de duas em duas

#ANALISE
print(len(frase)) #length -> número de caracteres
print(frase.count('o')) # conta quantas letras "o" tem na variavel frase
print(frase.count('o',0,14)) # conta quantas letras "o" nas posições entre 0 e 13
n1 = 'em'
print(frase.find(n1)) #encontra a posição de inicio da palavra "deo"
print(n1 in frase) # retorna verdadeiro pois em está contido em frase

#TRANSFORMAÇÃO
n2 = frase.replace('em', 'no') #substitui em por no
print(n2)
print(frase.upper()) #todas letras maiusculas
print(frase.lower()) #todas letras minusculas
print(frase.capitalize()) #primeira letra da frase maiucula
print(frase.title()) #todas primeiras letras das palavras maisculas

n3 = '     Tem espaços antes e depois     '
print(n3.strip()) #remove espaços antes e depois
print(n3.rstrip()) #remove espaços do lado direito
print(n3.lstrip()) #remove espacos do lado esquerdo

#DIVISÃO
print(frase.split()) #divide a frase transformado-a em lista onde ouver espaços

#JUNÇÃO
print('-'.join(frase)) #onde houver espaço é substituido por 'texto'


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