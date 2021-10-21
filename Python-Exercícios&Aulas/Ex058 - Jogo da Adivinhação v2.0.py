from random import randint
com = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar de um número entre 0 e 10')
print('Será que você vai conseguir adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jog = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jog == com:
        acertou = True
    else:
        if jog < com:
            print('Mais... Tente mais uma vez.')
        elif jog > com:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. PARABÉNS!'.format(palpites))