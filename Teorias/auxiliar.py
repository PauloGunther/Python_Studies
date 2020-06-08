def leiaIdade():
    while True:
        try:
            i = int(input('Digite a idade: '))
        except BaseException:
            print('Por favor digite um valor inteiro valido.')
        else:
            break
    return i


def linhas(tam=35):
    return print('-' * tam)


def cabecalho(txt):
    a = str(txt).upper()
    linhas()
    print(a.center(35))
    linhas()


def menu(lista, a):
    while True:
        cabecalho('menu principal')
        c = 1
        for i in lista:
            print(f'{c} - {i}')
            c += 1
        linhas()
        while True:
            try:
                opc = int(input('Qual opção deseja? '))
            except BaseException:
                print('Opção invalida. Tente novamente.')
            else:
                if opc > 3 or opc < 1:
                    print('Opção invalida. Tente novamente')
                else:
                    break
        if opc == 1:
            mostrar(a)
        elif opc == 2:
            cadastro(a)
        elif opc == 3:
            break
    print('Até logo.')


def cadastro(a):
    cabecalho('cadastro')  
    nome = str(input('Nome:'))
    idade = leiaIdade()
    arq = open(f'{a}', 'a')
    arq.write(f'{nome} {idade}\n')
    arq.close()


def mostrar(a):
    from time import sleep
    arq = open(f'{a}', 'r')
    linhas()
    print(f'{"NOME":<25}{"IDADE":<3}')
    linhas()
    for i in arq:
        linha = i.split()
        print(f'{linha[0]:<25}{linha[1]:>3} anos')
    sleep(1)
    arq.close()
