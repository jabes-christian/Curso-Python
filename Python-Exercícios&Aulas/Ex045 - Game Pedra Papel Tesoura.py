from random import randint
from time import sleep
itens = ['pedra', 'papel', 'tesoura']
com = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*15)
print('Computador jogou {}'.format(itens[com]))
print('Jogador escolheu {}'.format(itens[jog]))
print('-='*15)
if com == 0: # computador jogou PEDRA
    if jog == 0:
        print('EMPATE!')
    elif jog == 1:
        print('JOGADOR VENCEU!')
    elif jog == 3:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif com == 1: # computador jogou PAPEL
    if jog == 0:
        print('COMPUTADOR VENCE!')
    elif jog == 1:
        print('EMPATE!')
    elif jog == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif com == 2: # computador jogou TESOURA
    if jog == 0:
        print('JOGADOR VENCEU!')
    elif jog == 1:
        print('COMPUTADOR VENCEU!')
    elif jog == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
