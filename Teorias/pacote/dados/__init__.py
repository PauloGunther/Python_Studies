
def leiaDinheiro(a):
    while True:
        a = input('Digite o preço: R$ ') .replace(',', '.')
        if a.isalpha() or a == '':
            print(f'ERRO! {a} é um preço inválido.')
        else:
            return float(a)
            break


def leiaInt():
    while True:
        try:
            i = int(input('Digite um valor inteiro: '))
        except KeyboardInterrupt:
            print('O usuario preferiu não digitar esse número')
            i = 0
            break
        except:
            print('Por favor digite um valor inteiro valido.')
        else:
            break
    return i


def leiaFloat():
    while True:
        try:
            i = float(input('Digite um valor real: '))
        except KeyboardInterrupt:
            print('O usuario preferiu não digitar esse número')
            i = 0
            break
        except:
            print('Por favor digite um valor real valido.')
        else:
            break
    return i
