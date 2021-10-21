a = float(input('Quantos dias o carro foi alugado? '))
r = float(input('Quantos km rodados? '))
pago = (a * 60) + (r * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
