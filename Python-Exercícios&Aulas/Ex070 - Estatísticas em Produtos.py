print('{:-^40}'.format(' LOJA SUPER BARATÃO'))
soma = quant = menor = cont = 0
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    soma += preço
    if preço >= 1000:
        quant += 1
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {quant} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi a {barato} que custa R${menor:.2f}')
