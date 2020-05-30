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
