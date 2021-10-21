# Ex051
print('{:=^100}'.format('\n       10 TERMOS DE UM PA       \n'))
pri = int(input('Primeiro termo: '))
raz = int(input('razão: '))
dec = pri + (10 - 1) * raz
for c in range(pri, dec, raz):
    print('{}'.format(c), end=' > ')
print('ACABOU')
# Ex052
'''num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')'''
