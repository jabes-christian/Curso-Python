r = 'Ss'
soma = quant = média = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    quant += 1
    soma += n
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            n = maior
        if n < menor:
            n = menor
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {:.2f}'.format(n, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
