temp = list()
princ = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERROR! Digite novamente!')
    if r == 'N':
        break
print('-='*20)
print(f'Ao todo, você cadastrou {len(princ)} elementos')
print(f'O maior peso foi de de {maior}. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi de {menor}. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}')
print()

