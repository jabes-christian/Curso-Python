import random
a1 = input('Primeiro Aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto Aluno: ')
list = [a1, a2, a3, a4]
sort = random.choice(list)
print('O aluno escolhido foi {}'.format(sort))
print('-'*20)
from random import shuffle
n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')
lis = [n1, n2, n3 ,n4]
shuffle(lis)
print('A ordem de apresentação será')
print(lis)
