from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a de {:.2f}'.format(num, floor(raiz)))
print('-'*20)

import emoji
print(emoji.emojize('Olá Mundo :poop:', use_aliases=True))
