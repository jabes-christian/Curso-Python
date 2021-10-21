# Fatorial 1 forma 'while'
from math import factorial
n = int(input('Digite um número para\ncalcular sua fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

# Fatorial 2 forma 'while'
n = int(input('Digite um número para\ncalcular sua fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x '  if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

# Fatorial 3 forma 'for'
from math import factorial
n = int(input('Digite um número para\ncalcular sua factorial: '))
f = factorial(n)
print('Calculando {}! = '.format(n), end='')
for c in range(n, 0):
    print('{}'.format(c), end='')
print('{}'.format(f))

