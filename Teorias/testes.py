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
    while len(grupo) <= a or a < 0:
        print(f'ERRO! \nCódigo {a} não existe. Tente novamente.')
        a = int(input('Mostrar os dados de qual jogador: '))
    print(f'LEVANTAMENTO DO JOGADOR: {grupo[a]["nome"]}')
    partida = 1
    for c in grupo[a]['gols']:
        print(f'No jogo {partida} fez {c} gols')
        partida += 1

print(grupo)


