def leiaInt():
    while True:
        try:
            i = int(input('Digite um valor inteiro: '))
        except:
            print('Por favor digite um valor inteiro valido.')
        else:
            break
    return i