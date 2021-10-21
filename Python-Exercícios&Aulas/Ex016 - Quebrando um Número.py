from math import trunc
print('Primeira Maneira')
print('-'*20)
num = float(input('Digite um número: '))
inte = trunc(num)
print('O número {} tem a parte inteira {}'.format(num, inte))
print('-'*20)

print('Segunda Maneira')
print('-'*20)

import math
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num, math.trunc(num)))
print('-'*20)

print('Terceira Maneira')
print('-'*20)
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num, int(num)))


