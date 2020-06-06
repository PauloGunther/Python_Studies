from pacote import moeda
from pacote import dados

p1 = float(input('Digite o preco: R$ '))
print(f'A metade de {moeda.real(p1)} é {(moeda.metade(p1, True))}')
print(f'O dobre de {moeda.real(p1)} é {moeda.dobro(p1, True)}')
print(f'O valor aumentado 10% é {moeda.aumentar(p1, 10, True)}')
print(f'O valor diminuido 20% é {moeda.diminuir(p1, 20, True)}')


p2 = dados.leiaDinheiro('Digite o preco: R$ ')
moeda.resumo(p2, 50, 25)
