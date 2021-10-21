# Ex046
'''from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM! BUM! POOOW!')'''
# Ex047
'''for c in range(2, 51, 2):
    print(c, end=' ')
print('Acabou')'''
# Ex048
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
# Número par
soma = 0
cont = 0
for c in range(0, 1001, 2):
    if c % 4 == 0:
        cont += 1
        soma += c
print('A divisão de todos os {} valores solicitados {}'.format(cont, soma))
