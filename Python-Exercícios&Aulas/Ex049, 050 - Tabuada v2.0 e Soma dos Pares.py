# Ex049
n = int(input('Digite um número: '))
print('-='*20)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))

# Ex050
'''soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}° valor: '.format(c)))
    if c % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))'''
