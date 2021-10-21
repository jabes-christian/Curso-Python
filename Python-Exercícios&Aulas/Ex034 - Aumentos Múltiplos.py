sal = float(input('Qual é o salário do funcionário? R$'))
cores = {'amarelo':'\033[1;33m',
         'limpa':'\033[m'}
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('Quem ganhava {}R${:.2f}{} passa a ganhar {}R${:.2f}{} agora.'.format(cores['amarelo'], sal, cores['limpa'], cores['amarelo'], novo, cores['limpa']))
