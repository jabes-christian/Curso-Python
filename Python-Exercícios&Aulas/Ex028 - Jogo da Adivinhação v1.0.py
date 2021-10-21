from random import randint
from time import sleep
print('\033[33m''-=-''\033[m'*20)
print('\033[34m''Vou pensar entre um número entre 0 e 5. Tente adivinhar...''\033[m')
print('\033[33m''-=-''\033[m'*20)
com = randint(0, 5) # Faz o Jogador "PENSAR"
jog = int(input('Em que número eu pensei? ')) # Jogador tentar "ADIVINHAR"
print('\033[35m''PROCESSANDO...''\033[m')
sleep(3)
if jog == com:
    print('\033[32m''PARABÉNS! Você conseguiu me vencer!''\033[m')
else:
    print('\033[32m''GANHEI! Eu pensei no número {} e não no {}!''\033[m'.format(com, jog))
