from math import trunc, hypot

# MOSTRAR PARTE INTEIRA DE UM NÚMERO DECIMAL (TRUNC)
int = float(input('Digite um número decimal: '))
print('A parte inteira de {} é igual a {}' .format(int, trunc(int)))

# CALCULAR HIPOTENUSA (HYPOT)
ca = float(input('Digite o cateto adjacente em m²: '))
co = float(input('Digite o cateto oposto em m²: '))
print('A hipotenusa de {} m² e {} m² é igual a {:.2f} m².' .format(ca, co, hypot(ca, co)))

# CALCULAR SEN, COS, TAN DE UM ANGULO
from math import sin, cos, tan, radians
ang = float(input('Digite um angulo em graus: '))
print('O sen({:.0f}) é: {:.1f} \nO cos({:.0f}) é: {:.1f}\nA tg({:.0f}) é: {:.1f}'
      .format(ang, sin(radians(ang)), ang, cos(radians(ang)), ang, tan(radians(ang))))

# SORTEAR VALORES ALEATORIOS DE UMA LISTA
from random import choice
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
alunos = [a, b, c, d]
print('O sorteado é: {}'.format(choice(alunos)))

# ORDENAR ALEATORIAMENTE
from random import shuffle, sample
pacientes = 'Gabi Tuco Beto Chuva Borsa' .split()
shuffle(pacientes)
print('A ordem para receber a vacina é:\n{}' .format(pacientes))

# ORDENAR ALEATORIAMENTE UMA AMOSTRA DE UMA POPULACAO
paciente = ['A', 'B', 'C', 'D', 'E', 'F']
print('A ordem para receber a vacina é:\n{}' .format(sample(paciente, 4)))
