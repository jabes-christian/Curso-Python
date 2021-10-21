print('-='*20)
'''print('\033[1;34;43mOlá Mundo!\033[m')
print('\033[4;30;45mOlá Mundo!\033[m')
print('\033[30;41mOlá Mundo!\033[m')
print('\033[4;33;44mOlá Mundo!\033[m')
print('\033[1;35;43mOlá Mundo!\033[m')
print('\033[30;42mOlá Mundo!\033[m')
print('\033[37mOlá Mundo!\033[m')'''
# Primeiro Jeito de usar Cores
nome = 'Jabes'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto e branco':'\033[7;30m'}
print('Olá, muito prazer em te conhecer, {}{}{}'.format(cores['azul'], nome, cores['limpa']))
# Segundo jeito de usar Cores
print('-='*20)
nome = 'Jorge'
print('Olá, muito prazer em te conhecer, {}{}{}'.format('\033[4;32m', nome, '\033[m'))
