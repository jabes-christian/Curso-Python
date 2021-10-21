# Ex061 Progressão Aritmetica
'''print('Gerador de PA')
print('-='*10)
pri = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
termo = pri
cont = 1
while cont <= 10:
    print('{} >>> '.format(termo), end='')
    cont = cont + 1
    termo = termo + raz
print('FIM')'''
# Ex062 Super Progressão
print('Gerador de PA')
print('-='*10)
pri = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
termo = pri
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} >>> '.format(termo), end='')
        termo += raz
        cont += 1
        print('PAUSA')
        mais = int(input('Quantos termos você c quer mostra a mais: '))
print('FIM')