peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif imc >= 25 and imc < 30:
    print('Você está ACIMA DO PESO.')
elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE.')
elif imc > 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
