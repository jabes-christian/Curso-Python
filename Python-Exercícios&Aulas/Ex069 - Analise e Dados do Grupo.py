print('-'*30)
print('     CADASTRE UMA PESSOA')
print('-'*30)
tot18 = toth = totmulher20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    print('-'*25)
    if idade >= 18:
        tot18 += 1
    if sexo in 'M':
        toth += 1
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos ')