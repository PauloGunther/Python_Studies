print('='*10, 'Bem vindo ao nosso Banco!', '='*10)
vlr = float(input('Qual o valor da casa que você está querendo comprar? '))
slr = float(input('Informe seu salário, por favor: '))
t = int(input('Em quantos anos pretende pagar: '))

parcela = vlr / (12*t)

if parcela >= 0.3*slr:
    print('Empréstimo negado. A parcela excede é {:.1f}% do seu salário.' .format(100*parcela/slr))
else:
    print('Empréstimo confirmado. A parcela é {:.1f}% do seu salário.' .format(100*parcela/slr))
print('Tenha um bom dia!')

#QUAL É MAIOR
x1 = int(input('Digite um número inteiro: '))
x2 = int(input('Digite outro valor inteiro: '))

if x1>x2:
    print('O valor {}{}{} é maior' .format('\033[1;32m', x1, '\033[m'))
elif x2>x1:
    print('O valor {}{}{} é maior'.format('\033[1;32m', x2, '\033[m'))
else:
    print('Os valores são iguais!')

#IDADE DE ALISTAMENTO

from datetime import date
ano = int(input('Informe o ano que você nasceu: '))
if date.today().year - ano < 18:
    print('Você deverá se alistar somente daqui {} anos.' .format(18 + ano - int(date.today().year)))
elif date.today().year - ano > 18:
    print('Já passou {}  anos da hora de você se alistar.' .format(abs(18 + ano - int(date.today().year))))
else:
    print('Você deve se alistar este ano!')
print('O exercito brasileiro quer você!')

#CATEGORIAS NATAÇÃO

ano = int(input('Informe o ano que você nasceu: '))
if date.today().year - ano < 9:
    print('Categoria \033[1;31mMirim\033[m')
elif date.today().year - ano < 14:
    print('Categoria \033[1;31mInfantil\033[m')
elif date.today().year - ano < 19:
    print('Categoria \033[1;31mJunior\033[m')
else:
    print('Categoria \033[1;31mSenior\033[m')


#TRIANGULO É EQUILATERO
x1 = int(input('Digite um número: '))
x2 = int(input('Digite outro número: '))
x3 = int(input('Digite mais um número: '))

if abs(x1-x2) < x3 < x1+x2 and abs(x1-x3) < x2 < x1+x3 and abs(x3-x2) < x1 < x3+x2:
    print('O trinagulo existe!')
    if x1 == x2 == x3:
        print('Triangulo Equilatero')
    elif x1 == x2 or x3 == x1 or x3 == x2:
        print('Triangulo Isóceles')
    else:
        print('Triangulo Escaleno')
else:
    print('O triangulo não existe.')
