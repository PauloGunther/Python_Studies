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
def soma(a=0, b=0, c=0):  # quando igualado a 0 o parametro se torna opocional
    """
        Faz a soma de 3 valores e mostra o resultado na tela
        :param a:
        :param b:
        :param c:
    """
    s = a + b + c
    print(f'A soma vale {s}')


soma(2, 4)  # pode-se colocar de 0 a 3 parametros, pois todos são opcionais
soma(2)
soma()  # nao dará erro


# ESCOPO LOCAL E GLOBAL
def teste():
    x = 5  # x é uma variavel de escopo local, pois funcionará apenas dentro da função
    print(f'O valor de x vale {x}.')
    print(f'O valor de y vale {y}.')  # variavel global funciona dentro da função


y = 10  # variavel escopo global funciona dentro e fora da função
teste()
print(f'O valor x é {x}.')  # ERRO pois x é uma variavel local, nao funciona fora do funcao


def funcao1():  # podemos ter uma variavel valendo dois valores
    n1 = 4  # um valor de escopo local
    print(f'N1 dentro vale {n1}')  # ira printar 4


n1 = 2  # um outro valor de escopo global
print(f'N1 fora vale {n1}')  # ira printar 2
funcao1(n1)


def funcao2(n2):  # não entendi direito
    global n1  # supostamente é para puxar a valor global de n1
    n1 = 4
    n2 = 2*n1
    print(f'N1 dentro vale {n1}')
    print(f'N2 dentro valr {n2}')


n1 = 2
print(f'N1 fora vale {n1}')
funcao2(n1)


# RETURN
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s  # dessa forma pode-se manipular a resposta da funcao


a1 = somar(2, 3, 5)
a2 = somar(2, 2)
a3 = somar(6)

print(f'O valores das somas são {a1}, {a2} e {a3}.')


# EXEMPLOS
def fatorial(num=1):  # se o valor nao for informado assumira valor de 1
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


a1 = int(input('Digite um número: '))
print(f'O fatorial de {a1} vale {fatorial(a1)}.')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


a2 = int(input('Digite um número: '))
if par(a2):
    print('É par')
else:
    print('É impar')
