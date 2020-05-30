#CONDIÇÕES SE

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))

from statistics import mean #média importada
m = mean([n1, n2, n3])
print('Sua média é: {:.2f}' .format(m))

if m >= 7: # se a média for maior que 7
    print('Congrats, aprovado!') #precisa ser escrito com tab, pois esta subordinado ao IF
else: # se não for maior que 7
    print('Burro pra caralho!') #precisa ser escrito com tab, pois esta subordinado ao ELSE

nome = str(input('Qual o seu nome? '))
if nome == 'Paulo':
    print('Que nome bonito!') #CONDIÇÃO SIMPLES não precisa do else (se não)
print('Tenha um bom dia, {}.' .format(nome)) #condição que sempre vai ocorrer pois esta fora do if

nome = str(input('Qual o seu nome? '))
if nome == 'Paulo':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal') #ESTRUTURA CONDICIONAL COMPOSTA
print('Tenha um bom dia, {}.' .format(nome)) #como esta fora do tab irá ocorrer de qualquer maneira

nome = str(input('Qual o seu nome? '))
if nome == 'Paulo':
    print('Que nome bonito!')
elif nome =='Pedro' or nome== 'Ana': #funciona como outra condição se, que nao esta subordinada a primeira
    print('Seu nome é popular no Brasil!.')
elif nome in ('Ana Cláudia Jéssica Ellen'):
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal') #ESTRUTURA CONDICIONAL ANINHADA - ha varias condições
print('Tenha um bom dia, {}.' .format(nome))

