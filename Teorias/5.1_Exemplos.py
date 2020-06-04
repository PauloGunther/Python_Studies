#AREA DO TERRENO

def area(x, y):
    a = x * y
    print(f'A area de um terreno {x}x{y} é de {a:.2f}m².')

a = float(input('Comprimento: '))
b = float(input('Largura: '))
area(a, b)
#FORMACATAO ACOMAPNHA TEXTO

def form(texto):
    tamanho =len(texto)
    print('-'*(tamanho+5))
    print('{:^f}'.format(texto))
    print('-'*(tamanho+5))

form('MATRIX')
