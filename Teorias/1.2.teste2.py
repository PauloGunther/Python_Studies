import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {:.2f}.' .format(num, raiz))
print('E elevado a {} o resultado é {}' .format(2.5, math.ceil(num**num)))

#para economizar memória pode-se usar :

from math import sqrt, floor
num2 = float(input('digite um número: '))
raiz2 = sqrt(num)
print('A raiz de {} é igual a {}' .format(num2, floor(raiz2)))

import emoji
print(emoji.emojize('Python is :snowman:'))
