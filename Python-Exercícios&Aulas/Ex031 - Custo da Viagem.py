d = float(input('Qual é a distância de sua viagem: '))
cores = {'amarelo':'\033[33m',
         'azul':'\033[34m',
         'limpa':'\033[m'}
print('\033[31m''Você está prestes a começar uma viagem de {}{}km{}.''\033[m'.format(cores['amarelo'], d, cores['limpa']))
if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45
'''p = d * 0.50 if d <= 200 else d * 0.45'''
print('\033[31m''E o preço da sua passagem é de {}R${:.2f}{}!''\033[m'.format(cores['azul'], p, cores['limpa']))
