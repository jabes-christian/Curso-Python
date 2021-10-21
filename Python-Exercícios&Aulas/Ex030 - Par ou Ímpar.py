n = int(input('\033[35m''Me diga um número qualquer: ''\033[m'))
r = n % 2
if r == 0:
    print('O número {} é''\033[34m'' PAR!'.format(n))
else:
    print('O número {} é''\033[34m'' ímpar!'.format(n))
