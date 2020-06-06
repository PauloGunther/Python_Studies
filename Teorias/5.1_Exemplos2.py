# VOTO
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return print(f'Com {idade} anos: VOTO NEGADO.')
    elif 16 <= idade < 18 or idade > 60:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATORIO.')


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))


# FATORIAL
def fatorial(a, show=False):
    """
        Calcula o fatorial do valor
        param: a: valor a ser calculado
        param: show: (bool opcional)  mostra o calculo
        return: resultado no fatorial
    """
    f = 1
    for i in range(a, 0, -1):
        f *= i
        if show:
            if i == 1:
                print(f'{i} = ', end='')
            else:
                print(f'{i} x ', end='')
    return f


print(fatorial(5))
help(fatorial)


# JOGADOR
def ficha(a='<desconhecido>', b=0):
    print(f'O jogador {a} fez {b} gol(s).')


nome = str(input('Nome do jogador: ')) .strip()
gols = str(input('Número de gols: ')) .strip()
if gols == '':
    gols = int(0)
if nome == '':
    ficha(b=gols)
else:
    ficha(nome, gols)


# APENAS NUMEROS INTEIROS
def leiaint(a):
    while True:
        inteiro = input(a)
        if inteiro.isdecimal():
            break
        else:
            print('\033[1;31mERRO! digite um número Válido!\033[m')
    return inteiro


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar {n}')


# NOTAS
def notas(*num, sit=False):
    """
       Funçao analisa as notas e situação de variaos alunos
       :param num: uma ou mais notas dos alunos
       :param sit: valor opcional, mostra ou não a situcao geral
       return: dicionário com varias informações da turma
    """
    cont = s = 0
    for c in num:
        cont += 1
        s += c
    if s / cont >= 7:
        sitstr = 'BOA'
    elif 7 > s / cont >= 5:
        sitstr = 'SATISFATORIA'
    else:
        sitstr = 'RUIM'
    turma = {}
    if sit:
        turma = {'total': len(num),
                 'maior': max(num),
                 'menor': min(num),
                 'média': s / cont,
                 'situação': sitstr
                 }
    else:
        turma = {'total': len(num),
                 'maior': max(num),
                 'menor': min(num),
                 'média': s / cont,
                 }
    return turma


resp = notas(5, 4, 4, sit=True)
print(resp)
