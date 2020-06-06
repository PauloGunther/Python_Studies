def aumentar(a, b, c=False):
    """
        Aumentar valor de acordo com a porcentagem informada
        :param a: valor a ser aumentado
        :param b: porcetem
        :param c: bool opcional - formata valor em R$
        :return: retorna o valor do aumento
    """
    aume = a * (1 + (b / 100))
    if c:
        return real(aume)
    else:
        return aume


def diminuir(a, b, c=False):
    """
       Diminuiu valor de acordo com a porcentagem
        :param a: valor a ser diminuido
        :param b: porcetem
        :param c: bool opcional - formata valor em R$
        :return: retorna o valor do diminuição
    """
    dimi = a * (1 - (b / 100))
    if c:
        return real(dimi)
    else:
        return dimi


def dobro(a, b=False):
    """
       Dobra o valor
        :param a: valor a ser dobrado
        :param b: bool opcional - formata valor em R$
        :return: retorna o valor dobrado
    """
    dob = a * 2
    if b:
        return real(dob)
    else:
        return dob


def metade(a, b=False):
    """
       Divide par a metade do valor
        :param a: valor a ser dividido
        :param b: bool opcional - formata valor em R$
        :return: retorna metade do valor
    """
    met = a / 2
    if b:
        return real(met)
    else:
        return met


def real(a):
    """
       formata valor para R$
        :param a: valor a ser formatado
        :return br: valor já formatado
    """
    br = str("R$ {:.2f}" .format(a)).replace('.', ',')
    return br


def resumo(a, b, c):
    """
       Mostra um relatorio de aumento, diminuicao, dobra e metade
        :param a: valor a ser manipulado
        :param b: porcetem a aumentar
        :param c: porcenretam a diminuir
        :return: retorna tabela com o resumo
    """
    print('-' * 30)
    print('  RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado:        {real(a):<9}')
    print(f'Dobro de preço:         {dobro(a, True):<9}')
    print(f'Metade de preço:        {metade(a, True):<9}')
    print(f'{b}% de aumento:        {aumentar(a, b, True):^9}')
    print(f'{c}% de redução:        {diminuir(a, c, True):<9}')
    print('-' * 30)
