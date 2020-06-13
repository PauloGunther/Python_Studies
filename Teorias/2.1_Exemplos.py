# POR TUDO MAIUSCULO E MINUSCULO, CONTA NUMERO DE LETRAS
nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
rep = nome.replace(' ', '')
print('O número de letra é: {}' .format(len(rep)))
n1 = nome.split()
print('Seu primeiro nome tem {} letras' .format(len(n1[0])))

# MOSTRAR DEZENAS CENTENAS MILHARES
n = int(input('Digite um número entre 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}' .format(u, d, c, m))

# ANALIsAR SE O NOME DA CIDADE COMEÇA COM SANTO
city = str(input('Digite o nome de sua cidade: ')).split()[0].capitalize()
print(city == 'Santo')

# ANALIsAR SE HÁ SILVA NO SEU NOME
n = str(input('Digite seu nome: ')).title().split()
print('Silva' in n)

# ANALIsAR POSIÇÕES DE UMA LETRA NUMA FRASE
a1 = str(input('Digite uma frase: ')).lower().lstrip()
x = a1[0]
print('A letra {} aparece {} vezes na frase.' .format(x.upper(), a1.count(x)))
print('A primeira letra {} aparece na posição {}.' .format(x.upper(), a1.find(x)))
print('A última letra {} aparece na posição {}.' .format(x.upper(), a1.rfind(x)))

# IDENTIFICAR POSIÇÕES DE PALAVRAS NUMA FRASE
n = str(input('Digite seu nome completo: ')) .title().split()
print('Seu primeiro nome é: {}' .format(n[0]))
print('Se último nome é: {}' .format(n[-1]))
