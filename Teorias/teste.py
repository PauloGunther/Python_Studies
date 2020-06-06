import aux

bd = open('Teorias/bd.txt', 'a')

while True:
    bd.write(str(input('Nome: ')))
    idade = aux.leiaInt('Digite sua idade: ')
    d = input(':')
    if not d == 's':
        break

