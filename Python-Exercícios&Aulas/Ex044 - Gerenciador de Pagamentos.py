print('{:=^40}'.format(' LOJAS FANHES '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opc = float(input('Qual é sua opção? '))
if opc == 1:
    total = preço - (preço * 10 / 100)
elif opc == 2:
    total = preço - (preço * 5 / 100)
elif opc == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcela de 2x de R${:.2f}'.format(parcela))
elif opc == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcelas = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcelas))
else:
    total = preço
    print('\033[31m''OPÇÃO INVÁLIDA''\033[m'' de pagamento. Tente novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
