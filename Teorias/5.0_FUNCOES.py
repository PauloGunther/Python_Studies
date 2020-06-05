# FUNCOES
# Automatizar rotinas

def lin():  # cria uma função chamada 'lin' - define
    print('-'*20)  # quando rodar o programa funçao nao sao executadas


# para deixar o codigo legivel deixar duas linhas de espaço entre a def e o programa principal
# programa principal
lin()  # chamo a funcao que eu defini para ser executada
print('TITULO GRANDE')
lin()
print('TITULO PEQUENO')

lin()
print('RODA PÉ')
lin()


def titulo(txt):  # colocando um parametro na funcao
    lin()  # posso por funcao dentro de outra funcao
    print(txt)  # o paramentro aparecera onde for chamado
    lin()


titulo('MATRIX')  # imprime a palavra matrix no meio de duas linhas
titulo('CLUBE DA LUTA')


def soma(a, b):  # dois parametros
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma vale {s}')


soma(4, 2)  # o comando vai executar conforme a ordem
soma(a=5, b=8)  # pode-se definiar qual parametro entrara na variavel
soma(b=2, a=50)  # pode-se alterar a ordem desde que estejam definidas


# desempacotamento parametros TUPLAS
def contador(*num):  # o asterico permite colocar varios numeros dentro do mesmo parametro
    for i in num:
        print(f'{i} ', end='')  # printar cada um dos valores na mesma linha
    print('Fim.')


contador(2, 4, 7)
contador(2, 1, 9, 6, 20)
contador(2, 1)


def menos(*y):  # o asterico permite colocar varios numeros dentro do mesmo parametro
    s = 0
    for i in y:
        s -= i
    print(f'A subtracao dos {y} é {s}')


menos(4, 5, 8, 9)


# empacotar parametros LISTA
def dobra(lst):  # funcao que ira dobrar os valores de uma lista
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 2, 8, -20]
dobra(valores)  # ira dobrar os valores acima
print(valores)


# DOCSTRINGS
#   Mostra ajuda de uma funcao criada
#   help(print) -> irá mostrar a docomuntacao da função print()
#   help(random) -> ira mostrar a documnetação da biblioteca random


def contador(i, f, p):  # abrir 3"s para descrever a ajuda da funcao criada
    """
        Faz uma contagem e mostra na tela.
        :param i: iniocio da contagem
        :param f: final da contagem
        :param p: passo da contagem
        :retur: sem retorno
    """
    c = i  # inicio do codigo da funcao
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM!')


# agora pode-se:
help(contador)  # irá mostrar o manual criado no terminal

# PARAMETROS OPCIONAIS

def =





