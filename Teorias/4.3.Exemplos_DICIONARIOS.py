#GUARDAR INFORMACAO NUM DICIONARIO
aluno = dict()
aluno['Nome'] = str(input('Nome:'))
aluno['Media'] = int(input('Media: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperacao'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
print(aluno)
print()
print('-'*50)
print()

#SORTEAR VALORES DE UM DADO
from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
print('O valores sorteados:')
for c in range(0,5):
    jogo[f'Jogador {c}'] = randint(0,6)
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('O ranking dos jogadores:')
ordenado = sorted(jogo.items(), key = itemgetter(1), reverse=True)
print(ordenado)
for k, v in enumerate(ordenado):
    print(f'{k+1}º o {v[0]} com {v[1]}')
    sleep(0.5)
print()
print('-'*50)
print()

#CADASTRAR VARIOS DADOS DO TRABALHADOR
from datetime import date
cadastro = dict()

cadastro['nome'] = str(input('Nome: ')) .title().strip()
cadastro['idade'] = date.today().year - int(input('Ano de nascimento: '))
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salario: R$'))
    cadastro['aposentadoria'] = cadastro['contratacao'] + 35
print(cadastro)

for k, v in cadastro.items():
    print(f'{k} tem valor {v}')
print()
print('-'*50)
print()

#APROVEITAMENTO DE UM JOGADOR
jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: ')) .strip().title()
n = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
gols = list()
s = 0
for c in range(0, n):
    p = int(input(f'Quantos gols na partida {c+1}: '))
    gols.append(p)
    jogador['gols'] = gols
    s += p
jogador['total'] = s
print('-'*50)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-'*50)

print(f'O jogador {jogador["nome"]} jogou {n} partidas.')
for p, v in enumerate(jogador['gols']):
    print(f'    => Na parida {p+1}, marcou {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')
print()
print('-'*50)
print()

#CADASTRO DICIONARIOS EM LISTA
pessoas = dict()
grupo = list()
s = cont = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo [M/F]: ')) .strip().upper()
    pessoas['idade'] = int(input('Idade: '))
    grupo.append(pessoas.copy())
    cont += 1
    s += pessoas['idade'] 
    decisao = str(input('Deseja continuar [S/N]: ')) .strip().upper()
    if decisao in 'N':
        break
print(f'O grupo tem {cont} pessoas.')
print(f'A media de idade é de {s/cont:.1f} anos.')
print(f'As mulheres cadastradas: ', end='')
for c in grupo:
    if c['sexo'] == 'F':
        print(f'{c["nome"]} ', end ='')
print()
for c in grupo:
    if c['idade'] > s/cont:
        for k, v in c.items():
            print(f'{k} = {v}; ', end = '')
        print()
print()
print('-'*50)
print()

# APROVEITAMENTO DE UM JOGADOR
jogador = dict()
grupo = list()
deci = 0
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')) .strip().title()
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    gols = list()
    s = 0
    for c in range(0, n):
        p = int(input(f'Quantos gols na partida {c+1}: '))
        gols.append(p)
        jogador['gols'] = gols
        s += p
    jogador['total'] = s
    grupo.append(jogador.copy())

    print('-'*50)
    deci = str(input('Deseja continuar? [S/N]: ')) .upper().strip()
    if deci == 'N':
        break
print('-'*45)
cod = 0
print(f'{"cod":<3} {"Nome":<15} {"Gols":<15} {"Total":<5}')
for c in grupo:
    print('{:<3} {:<15} {:<15} {:<5}' .format(cod, c["nome"], str(c["gols"]), c["total"]))
    cod += 1
print('-'*45)
while True:
    a = int(input('Mostrar os dados de qual jogador: '))
    if a == 999:
        break
    if a >= len(grupo):
        print(f'ERRO! \nCódigo {a} não existe. Tente novamente.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR: {grupo[a]["nome"]}')
        for i, c in enumerate(grupo[a]['gols']):
            print(f'No jogo {i+1} fez {c} gols')
    print('-'*45)        

print()
print('-'*50)
print()

