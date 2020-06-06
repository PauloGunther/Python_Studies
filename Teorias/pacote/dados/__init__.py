
def leiaDinheiro(a):
    while True:
        a = input('Digite o preço: R$ ') .replace(',', '.')
        if a.isalpha() or a == '':
            print(f'ERRO! {a} é um preço inválido.')
        else:
            return float(a)
            break
