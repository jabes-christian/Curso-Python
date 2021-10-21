from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
v = 0
while True:
    jog = int(input('Diga um valor: '))
    com = randint(0, 11)
    total = jog + com
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('-'*20)
    print(f'Você jogou {jog} e o computador {com}. Total de {total} ', end='')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    print('-' * 20)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 1 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos nogar novamente...')
    print('=-'*20)
print('=-'*15)
print(f'GAME OVER! Você venceu {v} vezes')
